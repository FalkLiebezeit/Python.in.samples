import socket
import sqlite3
import pandas as pd
from datetime import datetime

def get_printer_settings(ip_address, port=9100):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((ip_address, port))
            s.sendall(b'^XA^HH^XZ')
            data = s.recv(4096)
        lines = data.decode('iso-8859-1').split('\n')

        darkness_setting = "Nicht gefunden"
        label_counter = None
        for line in lines:
            if "Schwärzung" in line and darkness_setting == "Nicht gefunden":
                darkness_setting = line.split(':')[-1].strip()
            elif "Zä.ni.rücks" in line and label_counter is None:
                label_counter_value = line.split(':')[-1].strip()
                label_counter_value = label_counter_value.replace('Zä.ni.rücks.', '').replace('Etiketten', '').replace(',', '').strip()
                if label_counter_value.isdigit():
                    label_counter = int(label_counter_value)
                    break  # Beendet die Schleife nach dem ersten gefundenen Wert

        return darkness_setting, label_counter
    except Exception as e:
        print(f"Fehler bei der Verbindung zum Drucker {ip_address}: {e}")
        return "Verbindungsfehler", None



# Liste von IP-Adressen der Drucker
printer_ips = ["12.0.1.115", "12.0.1.116","12.0.1.117", "12.0.1.118","12.0.1.119", "12.0.1.120","12.0.1.121", "12.0.1.122","12.0.1.123", "12.0.1.124","12.0.1.125", "12.0.1.126","12.0.1.127", "12.0.1.128","12.0.1.129", "12.0.1.130","12.0.1.131", "12.0.1.132","12.0.1.133", "12.0.1.134","12.0.1.135", "12.0.1.136","12.0.1.137", "12.0.1.138","12.0.1.139", "12.0.1.140","12.0.1.141","12.0.1.142","10.24.10.134", "12.0.1.160", "12.0.1.161","12.0.1.162", "12.0.1.163", \
               "12.0.1.164", "12.0.1.165","12.0.1.166", "12.0.1.167","12.0.1.168", "12.0.1.169", "12.0.1.171","12.0.1.172", "12.0.1.173","12.0.1.174", "12.0.1.175","12.0.1.176", "12.0.1.177","12.0.1.178", "12.0.1.179","12.0.1.180", "12.0.1.181","12.0.1.182","12.0.1.183", "12.0.1.184","12.0.1.185", "12.0.1.186","12.0.1.187"]  # Beispiel-IPs

# Daten sammeln und in einen DataFrame konvertieren
data = []
for ip in printer_ips:
    settings, counter = get_printer_settings(ip)
    data.append({"IP-Adresse": ip, "Schwärzungseinstellung": settings, "Etikettenzähler": counter})
df = pd.DataFrame(data)



# Daten in eine Excel-Datei schreiben
df.to_excel("drucker_einstellungen1.xlsx", index=False)

# Excel-Datei lesen
df = pd.read_excel("drucker_einstellungen1.xlsx")

# Aktuelle Etikettenzähler abfragen und Differenz berechnen
for index, row in df.iterrows():
    _, current_counter = get_printer_settings(row['IP-Adresse'])
    # Überprüfen, ob current_counter und Etikettenzähler gültige Werte sind
    if current_counter is not None and isinstance(current_counter, int) and \
       isinstance(row['Etikettenzähler'], int):
        df.at[index, 'Aktueller Etikettenzähler'] = current_counter
        df.at[index, 'Differenz Etikettenzähler'] = current_counter - row['Etikettenzähler']
        df['Aktueller Etikettenzähler'] = df['Aktueller Etikettenzähler'].astype(str)
        df['Differenz Etikettenzähler'] = df['Differenz Etikettenzähler'].astype(str)
    else:
        df.at[index, 'Aktueller Etikettenzähler'] = "Fehler"
        df.at[index, 'Differenz Etikettenzähler'] = "Fehler"

# Ergebnis in eine neue Excel-Datei speichern
df.to_excel("aktualisierte_drucker_einstellungen.xlsx", index=False)

# Laden der Daten aus drucker_einstellungen1.xlsx
df = pd.read_excel("drucker_einstellungen1.xlsx")

import sqlite3
import pandas as pd
from datetime import datetime

def datetime_to_string(dt_obj):
    """Konvertiert ein datetime Objekt in einen String."""
    return dt_obj.strftime("%Y-%m-%d %H:%M:%S")

# Daten aus der Excel-Datei laden
df = pd.read_excel("drucker_einstellungen1.xlsx")

# Versuche, eine Verbindung zur SQLite-Datenbank herzustellen
try:
    conn = sqlite3.connect('etikettenzaehler.db')
    cursor = conn.cursor()

    # Daten aus dem DataFrame in die Datenbanktabelle einfügen
    for index, row in df.iterrows():
        zeit = datetime_to_string(datetime.now())  # Konvertiert den aktuellen Zeitstempel in einen String
        ip_adresse = row['IP-Adresse']
        zaehlerstand = row['Etikettenzähler']

        # Überprüfen, ob zaehlerstand eine gültige Zahl ist
        if isinstance(zaehlerstand, int):
            cursor.execute('''
                INSERT INTO etikettenzaehler (zeit, ip_adresse, zaehlerstand) 
                VALUES (?, ?, ?)
            ''', (zeit, ip_adresse, zaehlerstand))

    # Änderungen speichern und Verbindung schließen
except sqlite3.Error as e:
    print(f"Fehler bei der Verbindung zur Datenbank: {e}")

    # Überprüfen, ob zaehlerstand eine gültige Zahl ist
    if isinstance(zaehlerstand, int):
        cursor.execute('''
            INSERT INTO etikettenzaehler (zeit, ip_adresse, zaehlerstand) 
            VALUES (?, ?, ?)
        ''', (zeit, ip_adresse, zaehlerstand))

# Änderungen speichern und Verbindung schließen
conn.commit()
conn.close()

