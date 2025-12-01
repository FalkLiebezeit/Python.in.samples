import socket
import pandas as pd

def clean_text(text):
    # Entfernt unzulässige Zeichen aus dem Text
    return ''.join(char for char in text if char.isprintable())

def get_printer_settings(ip_address, port=9100):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((ip_address, port))
            s.sendall(b'''^XA^JT1,Y,0,0~HQJT^XZ''')
            data = s.recv(4096)
        return clean_text(data.decode('iso-8859-1'))
    except Exception as e:
        print(f"Fehler bei der Verbindung zum Drucker {ip_address}: {e}")
        return f"Fehler: {e}"

# Liste von IP-Adressen der Drucker
printer_ips = ["10.24.10.135"]  # Beispiel-IPs

# Daten in eine Liste speichern
data = []
for ip in printer_ips:
    settings = get_printer_settings(ip)
    data.append({"IP-Adresse": ip, "Druckereinstellungen": settings})

# Daten in einen DataFrame konvertieren
df = pd.DataFrame(data)

# DataFrame in eine Excel-Datei schreiben
excel_filename = "drucker_einstellungen.xlsx"
df.to_excel(excel_filename, index=False)

print(f"Die Daten wurden in {excel_filename} gespeichert.")
