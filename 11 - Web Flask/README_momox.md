# momox.db Tags Viewer - Flask Web App

## Beschreibung
Diese Flask-Anwendung zeigt alle Daten aus der "Tags"-Tabelle der SQLite-Datenbank "momox.db" in einer übersichtlichen Weboberfläche an.

## Voraussetzungen
- Python 3.x
- Flask

## Installation

### 1. Flask installieren
```bash
pip install flask
```

Oder im virtuellen Environment:
```bash
python -m venv venv
venv\Scripts\activate  # Windows
pip install flask
```

### 2. Datenbank vorbereiten
Stellen Sie sicher, dass die Datei `momox.db` im gleichen Verzeichnis wie `momox_tags_viewer.py` liegt.

## Verwendung

### App starten
```bash
python momox_tags_viewer.py
```

Die Anwendung läuft dann auf: http://localhost:5000

### Verfügbare Routen
- `/` - Hauptseite mit formatierten Tabellendaten
- `/raw` - Rohdatenansicht als Liste

## Features
✅ Automatische Anzeige aller Spalten der Tags-Tabelle
✅ Responsive Design mit modernem UI
✅ Fehlerbehandlung bei fehlender Datenbank
✅ Hover-Effekte für bessere Lesbarkeit
✅ Alternativansicht mit Rohdaten

## Struktur
```
11 - Web Flask/
├── momox_tags_viewer.py    # Hauptanwendung
├── templates/
│   └── tags.html           # HTML-Template
└── momox.db                # SQLite-Datenbank (muss vorhanden sein)
```

## Hinweise
- Die App sucht automatisch nach `momox.db` im gleichen Verzeichnis
- Falls die Datenbank nicht gefunden wird, erscheint eine entsprechende Warnung
- Die App verwendet `sqlite3.Row` für einfachen Zugriff auf Spaltennamen
- Debug-Modus ist aktiviert für Entwicklungszwecke

## Troubleshooting

### Fehler: "Datenbankfehler"
- Überprüfen Sie, ob `momox.db` im richtigen Verzeichnis liegt
- Stellen Sie sicher, dass die Tabelle "Tags" in der Datenbank existiert
- Prüfen Sie die Zugriffsrechte auf die Datenbankdatei

### Port bereits belegt
Falls Port 5000 bereits verwendet wird, ändern Sie in `momox_tags_viewer.py`:
```python
app.run(debug=True, host='0.0.0.0', port=5001)  # Anderen Port verwenden
```
