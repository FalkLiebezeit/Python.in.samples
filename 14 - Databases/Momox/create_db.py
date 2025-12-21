import sqlite3
import os

# Desktop-Pfad ermitteln
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
db_path = os.path.join(desktop_path, "Falk.db")

# Datenbank erstellen und verbinden
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

print(f"Datenbank erfolgreich erstellt: {db_path}")

# Verbindung schließen
conn.close()
