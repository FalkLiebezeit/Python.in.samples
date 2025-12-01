import socket

def print_barcode(ip_address, port, barcode_data):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((ip_address, port))
            s.sendall(barcode_data.encode('utf-8'))

    except Exception as e:
        print(f"Fehler beim Senden an den Drucker: {e}")

# IP-Adresse und Port des Druckers
printer_ip = "10.24.1.43"  # Ersetzen Sie dies durch die IP-Adresse Ihres Druckers
printer_port = 9100  # Standardport für Netzwerkdrucker, aber überprüfen Sie Ihre Drucker-Konfiguration

# ZPL Barcode Befehl
zpl_command = """
^XA
^KL4
^XZ
"""

# Barcode drucken
print_barcode(printer_ip, printer_port, zpl_command)
