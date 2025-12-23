"""
Jira Issue Monitor für Momox
Überwacht kontinuierlich neue Jira-Tickets und benachrichtigt per Sprachausgabe.
"""

import os
import time
from typing import List, Optional
import requests
from requests.auth import HTTPBasicAuth
from gtts import gTTS

# ===== KONFIGURATION =====
# Jira API Endpoints
JIRA_BASE_URL = 'https://momox.atlassian.net/rest/api/3'
JIRA_SEARCH_URL = f'{JIRA_BASE_URL}/search'

# Authentifizierung (aus Umgebungsvariablen laden)
JIRA_TOKEN = os.getenv('JIRA_API_TOKEN')
JIRA_EMAIL = os.getenv('JIRA_EMAIL')

if not JIRA_TOKEN:
    raise ValueError("JIRA_API_TOKEN Umgebungsvariable nicht gesetzt! Bitte setzen Sie: export JIRA_API_TOKEN='your_token'")
if not JIRA_EMAIL:
    raise ValueError("JIRA_EMAIL Umgebungsvariable nicht gesetzt! Bitte setzen Sie: export JIRA_EMAIL='user@example.com'")
AUDIO_OUTPUT_PATH = os.path.expanduser(os.getenv("AUDIO_OUTPUT_PATH", "~/output.wav"))
# Audio-Konfiguration
AUDIO_OUTPUT_PATH = "/home/momox/output.wav"
os.environ['AUDIODEV'] = 'default'
os.environ['LD_PRELOAD'] = '/usr/lib/x86_64-linux-gnu/libaoss.so'

# Monitoring-Konfiguration
PROJECT_KEY = 'LEJSD'
TARGET_STATUS = "To Do"
POLL_INTERVAL = 5  # Sekunden zwischen Abfragen
MAX_RESULTS = 10   # Maximale Anzahl der abzurufenden Issues

# HTTP-Header für Jira-API
HEADERS = {'Accept': 'application/json'}

print(f"AUDIODEV: {os.environ.get('AUDIODEV')}")
print(f"LD_PRELOAD: {os.environ.get('LD_PRELOAD')}")


def fetch_recent_issues() -> Optional[List[dict]]:
    """
    Ruft die neuesten Jira-Issues ab.
    
    Returns:
        Liste von Issues oder None bei Fehler
    """
    query = {
        'jql': 'ORDER BY created DESC',
        'maxResults': MAX_RESULTS,
        'fields': ['key', 'summary', 'status', 'created']
    }
    
    try:
        response = requests.get(
            url=JIRA_SEARCH_URL,
            params=query,
            headers=HEADERS,
            auth=HTTPBasicAuth(username=JIRA_EMAIL, password=JIRA_TOKEN),
            timeout=10
        )
        response.raise_for_status()
        data = response.json()
        return data.get('issues', [])
    except requests.RequestException as e:
        print(f"Fehler beim Abrufen der Issues: {e}")
        return None


def check_issue_status(issue_number: int) -> Optional[str]:
    """
    Überprüft den aktuellen Status eines Issues.
    
    Args:
        issue_number: Die Issue-Nummer (nur Zahl, ohne Projekt-Präfix)
    
    Returns:
        Status-String oder None bei Fehler
    """
    issue_key = f'{PROJECT_KEY}-{issue_number}'
    
    try:
        response = requests.get(
            url=f'{JIRA_BASE_URL}/issue/{issue_key}',
            headers=HEADERS,
            auth=HTTPBasicAuth(username=JIRA_EMAIL, password=JIRA_TOKEN),
            timeout=10
        )
        response.raise_for_status()
        data = response.json()
        return data.get('fields', {}).get('status', {}).get('name')
    except requests.RequestException as e:
        print(f"Fehler beim Abrufen von Issue {issue_key}: {e}")
        return None


def filter_open_issues(issues: List[dict]) -> List[int]:
    """
    Filtert Issues nach Projekt und Status "To Do".
    
    Args:
        issues: Liste der zu filternden Issues
    
    Returns:
        Liste der Issue-Nummern im Status "To Do"
    """
    open_issues = []
    
    for issue in issues:
        issue_key = issue['key']
        issue_status = issue['fields']['status']['name']
        
        # Issue-Key aufteilen (z.B. "LEJSD-123" -> ["LEJSD", "123"])
        parts = issue_key.split('-')
        
        if len(parts) == 2 and parts[0] == PROJECT_KEY and issue_status == TARGET_STATUS:
            issue_number = int(parts[1])
            print(f'[{issue_number}] gefunden!')
            open_issues.append(issue_number)
    
    return open_issues


def verify_issue_statuses(issue_numbers: List[int]) -> List[int]:
    """
    Verifiziert den Status jedes Issues und entfernt nicht mehr offene Issues.
    
    Args:
        issue_numbers: Liste der zu überprüfenden Issue-Nummern
    
    Returns:
        Liste der bestätigten offenen Issue-Nummern
    """
    verified_issues = []
    
    for issue_number in issue_numbers:
        status = check_issue_status(issue_number)
        print(f'Issue [{issue_number}] Status: {status}')
        
        if status == TARGET_STATUS:
            verified_issues.append(issue_number)
        else:
            print(f'[{issue_number}] wird entfernt ...')
    
    return verified_issues


def play_audio_notification(issue_count: int) -> None:
    """
    Erstellt und spielt eine Sprachbenachrichtigung ab.
    
    Args:
        issue_count: Anzahl der gefundenen Issues
    """
    if issue_count == 0:
        return
    
    # Grammatikalisch korrekte Nachricht erstellen
    text = f"{issue_count} neue Störung gefunden" if issue_count == 1 else f"{issue_count} neue Störungen gefunden"
    print(f"{issue_count} Issue(s) gefunden")
    
    try:
        # TTS-Datei erstellen
        tts = gTTS(text=text, lang='de')
        tts.save(AUDIO_OUTPUT_PATH)
        
        if os.path.exists(AUDIO_OUTPUT_PATH):
            print("Audio-Datei erfolgreich erstellt.")
            # Audio abspielen
            os.system(f'mpg321 {AUDIO_OUTPUT_PATH}')
        else:
            print("Fehler: Audio-Datei konnte nicht erstellt werden.")
    except Exception as e:
        print(f"Fehler bei der Audio-Wiedergabe: {e}")


def monitor_issues() -> None:
    """
    Hauptschleife: Überwacht kontinuierlich Jira-Issues und benachrichtigt bei neuen Tickets.
    """
    print(f"Starte Jira-Monitor für Projekt {PROJECT_KEY}...")
    
    while True:
        try:
            # Neueste Issues abrufen
            issues = fetch_recent_issues()
            
            if issues:
                # Nach offenen Issues filtern
                open_issues = filter_open_issues(issues)
                
                # Status jedes Issues verifizieren
                verified_open_issues = verify_issue_statuses(open_issues)
                
                # Bei gefundenen Issues Benachrichtigung abspielen
                play_audio_notification(len(verified_open_issues))
                
                print(f'Offene Tickets: {verified_open_issues}')
            
            # Wartezeit bis zur nächsten Abfrage
            time.sleep(POLL_INTERVAL)
            
        except KeyboardInterrupt:
            print("\nMonitoring beendet.")
            break
        except Exception as e:
            print(f"Unerwarteter Fehler: {e}")
            time.sleep(POLL_INTERVAL)


if __name__ == "__main__":
    monitor_issues()




