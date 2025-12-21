import sqlite3
import os

# Pfad zum Momox-Ordner
db_folder = r"C:\Users\Falk\source\repos\Python.in.samples\14 - Databases\Momox"
db_path = os.path.join(db_folder, "Falk.db")

# Datenbank erstellen und verbinden
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

print(f"Datenbank erfolgreich erstellt: {db_path}")

# Verbindung schließen
conn.close()
