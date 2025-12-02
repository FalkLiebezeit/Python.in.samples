import sqlite3
import pandas as pd
from datetime import datetime

def get_daily_data():
    conn = sqlite3.connect('etikettenzaehler.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT ip_adresse, DATE(zeit) as date, MIN(zeit) as min_time, MAX(zeit) as max_time, 
               MIN(zaehlerstand) as min_counter, MAX(zaehlerstand) as max_counter 
        FROM etikettenzaehler 
        GROUP BY ip_adresse, date
        ORDER BY ip_adresse, date
    ''')
    data = cursor.fetchall()
    conn.close()
    return data

def calculate_daily_etiketten(data):
    results = []
    for record in data:
        ip, date, min_time, max_time, min_counter, max_counter = record

        # Überprüfen und Anpassen des Datumsformats für min_time und max_time
        try:
            min_time = datetime.strptime(min_time, '%Y-%m-%d %H:%M:%S.%f')
        except ValueError:
            min_time = datetime.strptime(min_time, '%Y-%m-%d %H:%M:%S')

        try:
            max_time = datetime.strptime(max_time, '%Y-%m-%d %H:%M:%S.%f')
        except ValueError:
            max_time = datetime.strptime(max_time, '%Y-%m-%d %H:%M:%S')

        zeit_diff = (max_time - min_time).total_seconds() / 3600  # Zeitdifferenz in Stunden
        if zeit_diff > 0:
            etiketten_diff = max_counter - min_counter
            etiketten_pro_tag = round((etiketten_diff / zeit_diff) * 24)  # Umrechnung auf Etiketten pro Tag
            results.append({'IP-Adresse': ip, 'Datum': date, 'Etiketten/Tag': etiketten_pro_tag})

    return results

# Rest des Codes bleibt unverändert


# Daten abrufen und verarbeiten
daily_data = get_daily_data()
result_data = calculate_daily_etiketten(daily_data)

# Ergebnisse in DataFrame konvertieren und in Excel-Datei speichern
df_result = pd.DataFrame(result_data)
# Berechnung der Etiketten pro Tag
result_data = calculate_daily_etiketten(daily_data)

# Ergebnisse in einen DataFrame konvertieren
df_result = pd.DataFrame(result_data)

# Summe der Etiketten pro Tag berechnen
daily_sum = df_result.groupby('Datum')['Etiketten/Tag'].sum().reset_index()
daily_sum['IP-Adresse'] = 'Gesamtsumme'  # Zusätzliche Spalte für die Gesamtsumme


# Druckerauslastung berechnen
active_printers = df_result[df_result['Etiketten/Tag'] > 0]['IP-Adresse'].nunique()
total_printers = df_result['IP-Adresse'].nunique()
printer_utilization = active_printers / total_printers if total_printers > 0 else 0
printer_utilization_percentage = printer_utilization * 100

# Hinzufügen der Gesamtsumme und der Druckerauslastung in den DataFrame
df_final = pd.concat([df_result, pd.DataFrame([{}]), daily_sum], ignore_index=True)
df_final = pd.concat([df_final, pd.DataFrame([{'IP-Adresse': 'Druckerauslastung', 'Etiketten/Tag': f"{printer_utilization_percentage:.2f}%"}])], ignore_index=True)

# Speichern der neuen Daten in der Excel-Datei
df_final.to_excel("etiketten_pro_tag.xlsx", index=False)
