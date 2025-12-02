import sqlite3
from datetime import datetime

# Verbindung zur SQLite-Datenbank herstellen (wird erstellt, falls sie nicht existiert)
conn = sqlite3.connect('etikettenzaehler.db')

# Cursor-Objekt erstellen
cursor = conn.cursor()

# Tabelle etikettenzähler erstellen
cursor.execute('''
    CREATE TABLE IF NOT EXISTS etikettenzaehler (
        zeit TIMESTAMP,
        ip_adresse TEXT,
        zaehlerstand INTEGER
    )
''')