import socket
import pandas as pd
from concurrent.futures import ThreadPoolExecutor

def clean_text(text):
    # Entfernt unzulässige Zeichen aus dem Text
    return ''.join(char for char in text if char.isprintable())

def get_printer_settings(ip_address, port=9100):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((ip_address, port))
            s.sendall(b'''^XA~HQES^XZ''')
            data = s.recv(512)
        return clean_text(data.decode('iso-8859-1'))
    except Exception as e:
        return f"Fehler: {e}"

def fetch_printer_data(ip):
    settings = get_printer_settings(ip)
    return {"IP-Adresse": ip, "Druckereinstellungen": settings}

# Liste von IP-Adressen der Drucker
printer_ips =["12.0.1.115", "12.0.1.116","12.0.1.117", "12.0.1.118","12.0.1.119", "12.0.1.120","12.0.1.121", "12.0.1.122","12.0.1.123", "12.0.1.124","12.0.1.125", "12.0.1.126","12.0.1.127", "12.0.1.128","12.0.1.129", "12.0.1.130","12.0.1.131", "12.0.1.132","12.0.1.133", "12.0.1.134","12.0.1.135", "12.0.1.136","12.0.1.137", "12.0.1.138","12.0.1.139", "12.0.1.140","12.0.1.141","12.0.1.142","12.0.1.160", "12.0.1.161","12.0.1.162", "12.0.1.163", \
               "12.0.1.164", "12.0.1.165","12.0.1.166", "12.0.1.167","12.0.1.168", "12.0.1.169", "12.0.1.171","12.0.1.172", "12.0.1.173","12.0.1.174", "12.0.1.175","12.0.1.176", "12.0.1.177","12.0.1.178", "12.0.1.179","12.0.1.180", "12.0.1.181","12.0.1.182","12.0.1.183", "12.0.1.184","12.0.1.185", "12.0.1.186","12.0.1.187",
               "10.24.1.107", "10.24.1.97", "10.24.1.92", "10.24.1.96", "10.24.1.94", "10.24.1.93", "10.24.1.50", "10.24.1.51", "10.24.1.48", "10.24.1.49", "10.24.1.43", "10.24.1.42", "10.24.1.45", "10.24.1.44",
               "10.24.1.108", "10.24.1.109", "10.24.1.101", "10.24.1.100", "10.24.1.99", "10.24.1.98", "10.24.1.110", "10.24.1.102", "10.24.1.103", "10.24.1.104", "10.24.1.105", "10.24.1.106", "10.24.1.111", "10.24.1.95",
               "10.24.0.22"]

# Verwendung von ThreadPoolExecutor zur Parallelisierung
with ThreadPoolExecutor(max_workers=20) as executor:
    data = list(executor.map(fetch_printer_data, printer_ips))

# Daten in einen DataFrame konvertieren
df = pd.DataFrame(data)

# DataFrame in eine Excel-Datei schreiben
excel_filename = "drucker_einstellungen.xlsx"
df.to_excel(excel_filename, index=False)

print(f"Die Daten wurden in {excel_filename} gespeichert.")
