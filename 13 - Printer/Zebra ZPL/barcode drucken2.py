import socket

def print_barcode(ip_address, port, barcode_data):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((ip_address, port))
            s.sendall(barcode_data.encode('utf-8'))

    except Exception as e:
        print(f"Fehler beim Senden an den Drucker: {e}")

# IP-Adresse und Port des Druckers
#printer_ip = "10.24.1.192"  NLL Druckerplatz 15     US_201_R
#printer_ip = "10.24.1.193"  NLL Druckerplatz 16
#printer_ip = "10.24.1.194"  NLL Druckerplatz 17
#printer_ip = "10.24.1.195"  NLL Druckerplatz 18
printer_ip = "10.24.1.188"

# Ersetzen Sie dies durch die IP-Adresse Ihres Druckers
printer_port = 9100  # Standardport für Netzwerkdrucker, aber überprüfen Sie Ihre Drucker-Konfiguration

# ZPL Barcode Befehl
zpl_command = """
^XA
^PW815
^FX square that extends the entire label.
^FO2,2^GB808,1213,5^FS
^FX top left square
^FO2,2^GB50,50,5^FS
^CF0,30
^FO13,17^FDTL^FS

^FX top right square
^FO759,3^GB50,50,5^FS
^CF0,30
^FO767,17^FDTR^FS

^FX bottom left square
^FO2,1165^GB50,50,5^FS
^CF0,30
^FO12,1180^FDBL^FS

^FX bottom right square
^FO759,1165^GB50,50,5^FS
^CF0,30
^FO767,1180^FDBR^FS

^CF0,60
^FO110,80^FDMomox Leipzig Testlable^FS
^CF0,30
^FO235,165^FDFor testing the Zebra ZT230^FS



^FO0,260^GB830,100,100^FS


^FO20,645^FDPrinthead: check the horizontal bar across the entire label.^FS
^FO20,690^FDPage Setup: check the squares in the corners.^FS

^CF0,25
^FO135,1050^FDNote that the printed item was not routed via SendIT!^FS
^FO175,1080^FDThis Printing is the result of a plain ZPL File!^FS





^XZ
"""

# Barcode drucken
print_barcode(printer_ip, printer_port, zpl_command)
