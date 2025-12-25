"""
Flask Web App zur Anzeige aller Daten aus der Tags-Tabelle der momox.db Datenbank
"""

from flask import Flask, render_template
import sqlite3
import os

app = Flask(__name__)

# Pfad zur Datenbank
DB_PATH = os.path.join(os.path.dirname(__file__), 'momox.db')


def get_db_connection():
    """Erstellt eine Verbindung zur SQLite-Datenbank"""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # Ermöglicht Zugriff auf Spalten über Namen
    return conn


@app.route('/')
def index():
    """Hauptseite - zeigt alle Tags aus der Datenbank"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Alle Daten aus der Tags-Tabelle abrufen
        cursor.execute('SELECT * FROM Tags')
        tags = cursor.fetchall()
        
        # Spaltennamen ermitteln
        column_names = [description[0] for description in cursor.description]
        
        conn.close()
        
        return render_template('tags.html', tags=tags, columns=column_names)
    
    except sqlite3.Error as e:
        return f"<h1>Datenbankfehler</h1><p>Fehler beim Zugriff auf die Datenbank: {str(e)}</p><p>Stellen Sie sicher, dass die Datei 'momox.db' im gleichen Verzeichnis wie die App existiert.</p>"
    except Exception as e:
        return f"<h1>Fehler</h1><p>Ein Fehler ist aufgetreten: {str(e)}</p>"


@app.route('/raw')
def raw_data():
    """Zeigt die Rohdaten als einfache Liste"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM Tags')
        tags = cursor.fetchall()
        
        conn.close()
        
        result = "<h1>Tags - Rohdaten</h1>"
        result += f"<p>Anzahl der Einträge: {len(tags)}</p>"
        result += "<ul>"
        for tag in tags:
            result += f"<li>{dict(tag)}</li>"
        result += "</ul>"
        result += '<br><a href="/">Zurück zur formatierten Ansicht</a>'
        
        return result
    
    except sqlite3.Error as e:
        return f"<h1>Datenbankfehler</h1><p>{str(e)}</p>"


if __name__ == '__main__':
    # Überprüfen, ob die Datenbank existiert
    if not os.path.exists(DB_PATH):
        print(f"WARNUNG: Die Datenbank '{DB_PATH}' wurde nicht gefunden!")
        print("Bitte stellen Sie sicher, dass die Datei 'momox.db' im gleichen Verzeichnis existiert.")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
