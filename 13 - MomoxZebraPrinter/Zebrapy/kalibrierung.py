import socket
import pandas as pd

def get_printer_settings(ip_address, port=9100):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((ip_address, port))
            s.sendall(b'''^XA
                      ~SD22
                      ~JG
                      ^HH
                      ^XZ''')
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
printer_ips = ["10.24.10.134"]
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
