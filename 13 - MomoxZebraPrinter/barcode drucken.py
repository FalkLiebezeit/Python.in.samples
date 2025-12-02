import socket

def print_barcode(ip_address, port, barcode_data):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # Timeout einstellen, um zu verhindern, dass das Skript unbegrenzt wartet
            s.settimeout(10)  # 10 Sekunden Timeout

            # Verbindung zum Drucker herstellen
            s.connect((ip_address, port))
            print("Verbunden mit dem Drucker.")

            # Daten an den Drucker senden
            s.sendall(barcode_data.encode('utf-8'))
            print("Daten gesendet.")

            # Antwort vom Drucker abfangen, falls vorhanden
            try:
                response = s.recv(1024)
                print("Antwort vom Drucker erhalten:", response)
            except socket.timeout:
                print("Keine Antwort vom Drucker erhalten (Timeout).")
            except Exception as e:
                print("Fehler beim Empfangen der Antwort vom Drucker:", e)

    except Exception as e:
        print(f"Fehler beim Senden an den Drucker: {e}")

# IP-Adresse und Port des Druckers
printer_ip = "12.0.1.177"
printer_port = 9100  # Standardport für Netzwerkdrucker

# ZPL Barcode Befehl
zpl_command = """
^XA
^MUd,200,200
^KL4
^PON
^FO0,0
^BCN,120,Y,N,N,A
^FD12345678901234567890123456789012345678901234567890123456789012345678901234567890^FS
^FO0,150
^GB830,,160^FS
^FO0,320
^BCN,120,Y,N,N,A
^FDABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz^FS
^FO0,470
^GB830,,160^FS
^FO0,650
^BCN,120,Y,N,N,A
^FD12345678901234567890123456789012345678901234567890123456789012345678901234567890^FS
^FO0,800
^GB830,,160^FS
^FO0,970
^BCN,120,Y,N,N,A
^FDABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz^FS
^FO0,1120
^BCR,850,Y,N
^FD1^FS
^XZ
"""

# Druck 1 Mal ausführen
for _ in range(1):
    print_barcode(printer_ip, printer_port, zpl_command)
