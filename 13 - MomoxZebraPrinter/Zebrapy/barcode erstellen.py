import barcode
from barcode.writer import ImageWriter
from PIL import Image

def generate_barcode(data, barcode_filename):
    # Barcode-Klasse erhalten
    CODE128 = barcode.get_barcode_class('code128')

    # Überprüfen, ob die Barcode-Klasse korrekt geladen wurde
    if CODE128 is None:
        raise Exception("Barcode-Klasse konnte nicht geladen werden. Stellen Sie sicher, dass python-barcode installiert ist.")

    # Erstellen eines Barcodes
    barcode_obj = CODE128(data, writer=ImageWriter())

    # Speichern des Barcodes als Bild
    barcode_filepath = barcode_filename + '.png'
    barcode_obj.save(barcode_filepath)

    # Laden und Anzeigen des Bildes mit Pillow
    image = Image.open(barcode_filepath)
    image.show()

# Daten, die im Barcode kodiert werden sollen
data_to_encode = "1234567890"

# Dateiname, unter dem der Barcode gespeichert wird (ohne Dateiendung)
filename_for_barcode = "barcode"

generate_barcode(data_to_encode, filename_for_barcode)