import sqlite3

conn = sqlite3.connect('momox.db')
cursor = conn.cursor()

# Alle Tabellen anzeigen
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cursor.fetchall()
print("Verfügbare Tabellen:")
print("-" * 50)
for table in tables:
    print(table[0])

# Struktur der Tags-Tabelle
print("\n\nSpalten der Tags-Tabelle:")
print("-" * 50)
cursor.execute('PRAGMA table_info(Tags)')
columns = cursor.fetchall()
for col in columns:
    print(f"ID: {col[0]}, Name: {col[1]}, Type: {col[2]}, NotNull: {col[3]}, Default: {col[4]}, PK: {col[5]}")

# Beispieldaten
print("\n\nErste 3 Zeilen aus Tags:")
print("-" * 50)
cursor.execute('SELECT * FROM Tags LIMIT 3')
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()
