import sqlite3
import os
import pandas as pd
from datetime import datetime

def get_data_from_db():
    conn = sqlite3.connect('etikettenzaehler.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT ip_adresse, zeit, zaehlerstand 
        FROM etikettenzaehler 
        ORDER BY ip_adresse, zeit
    ''')
    data = cursor.fetchall()
    conn.close()
    return data

def calculate_etiketten_pro_stunde(data):
    result = []
    ip_records = {}  # Dictionary zum Speichern der letzten zwei Records pro IP

    for record in data:
        ip, zeit, zaehlerstand = record
        try:
            # Versuchen, das Datum mit Millisekunden zu parsen
            zeit = datetime.strptime(zeit, '%Y-%m-%d %H:%M:%S.%f')
        except ValueError:
            # Falls kein Millisekundenteil vorhanden ist, normales Format verwenden
            zeit = datetime.strptime(zeit, '%Y-%m-%d %H:%M:%S')

        if ip not in ip_records:
            ip_records[ip] = [(zeit, zaehlerstand)]
        else:
            ip_records[ip].append((zeit, zaehlerstand))
            if len(ip_records[ip]) > 2:
                ip_records[ip].pop(0)  # Entfernen des ältesten Eintrags, falls mehr als zwei vorhanden sind

    for ip, records in ip_records.items():
        if len(records) == 2:
            first_record, last_record = records
            zeit_diff = (last_record[0] - first_record[0]).total_seconds() / 3600
            if zeit_diff > 0:
                etiketten_diff = last_record[1] - first_record[1]
                etiketten_pro_stunde = round(etiketten_diff / zeit_diff)
                result.append({'IP-Adresse': ip, 'Zeit': last_record[0], 'Etiketten/Stunde': etiketten_pro_stunde})

    return result


# Daten aus der Datenbank abrufen
db_data = get_data_from_db()

# Berechnung der Etiketten pro Stunde
result_data = calculate_etiketten_pro_stunde(db_data)

# Ergebnisse in einen DataFrame konvertieren
df_result = pd.DataFrame(result_data)

# Dateiname der Excel-Datei
excel_file = "etiketten_pro_stunde.xlsx"

# Überprüfen, ob die Datei existiert, und sie löschen
if os.path.exists(excel_file):
    os.remove(excel_file)

# Speichern der neuen Daten in der Excel-Datei
df_result.to_excel(excel_file, index=False)