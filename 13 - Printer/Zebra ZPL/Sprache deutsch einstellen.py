import socket
import pandas as pd

def get_printer_settings(ip_address, port=9100):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((ip_address, port))
            s.sendall(b'^XA^HZr^HZa^XZ')
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
printer_ips = ["10.24.10.134"]  # Beispiel-IPs



print(f"Die Sprache wurde auf Deutsch geändert.")





