import socket
import pandas as pd

def get_printer_settings(ip_address, port=9100):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((ip_address, port))
            s.sendall(b'^XA^HH^XZ')
            data = s.recv(1024)
        lines = data.decode('iso-8859-1').split('\n')
        if len(lines) >= 2:
            return lines[1].strip()
        else:
            return "Keine ausreichenden Daten empfangen."
    except Exception as e:
        print(f"Fehler bei der Verbindung zum Drucker {ip_address}: {e}")
        return None

# Liste von IP-Adressen der Drucker
printer_ips = ["12.0.1.115", "12.0.1.116","12.0.1.117", "12.0.1.118","12.0.1.119", "12.0.1.120","12.0.1.121", "12.0.1.122","12.0.1.123", "12.0.1.124","12.0.1.125", "12.0.1.126","12.0.1.127", "12.0.1.128","12.0.1.129", "12.0.1.130","12.0.1.131", "12.0.1.132","12.0.1.133", "12.0.1.134","12.0.1.135", "12.0.1.136","12.0.1.137", "12.0.1.138","12.0.1.139", "12.0.1.140","12.0.1.141","12.0.1.142","10.24.10.134", "12.0.1.160", "12.0.1.161","12.0.1.162", "12.0.1.163", \
               "12.0.1.164", "12.0.1.165","12.0.1.166", "12.0.1.167","12.0.1.168", "12.0.1.169", "12.0.1.171","12.0.1.172", "12.0.1.173","12.0.1.174", "12.0.1.175","12.0.1.176", "12.0.1.177","12.0.1.178", "12.0.1.179","12.0.1.180", "12.0.1.181","12.0.1.182","12.0.1.183", "12.0.1.184","12.0.1.185", "12.0.1.186","12.0.1.187"]  # Beispiel-IPs

# Daten in eine Liste speichern
data = []
for ip in printer_ips:
    settings = get_printer_settings(ip)
    data.append({"IP-Adresse": ip, "Schwärzungseinstellung": settings})

# Daten in einen DataFrame konvertieren
df = pd.DataFrame(data)

# DataFrame in eine Excel-Datei schreiben
excel_filename = "drucker_einstellungen.xlsx"
df.to_excel(excel_filename, index=False)

print(f"Die Daten wurden in {excel_filename} gespeichert.")





