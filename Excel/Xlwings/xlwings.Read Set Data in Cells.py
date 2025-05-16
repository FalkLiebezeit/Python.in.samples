import os
import xlwings as xw




try:
    # Excel-Datei öffnen
    #
    # wb = xw.Book('C:\\Users\\Falk\\TestData\\TestZahlen.xlsx',update_links=False,read_only=True)


    file_path = os.path.join('C:\\Users\\Falk\\TestData', 'TestZahlen.xlsx')
    wb = xw.Book(file_path)


    sheet = wb.sheets['Datasheet1']

    # Wert aus Zelle C36 auslesen
    wert_C3 = sheet.range('C3').value

    #ws = wb.active

    # Wert der Zelle C37 auf 11 setzen
    sheet.range('C4').value = 11


    # Wert ausgeben
    print(f"Wert in C3: {wert_C3}")



    print("Berechnung erfolgreich abgeschlossen!")

except Exception as e:
    print(f"Fehler aufgetreten: {e}")

finally:
    wb.save()
    wb.close()


