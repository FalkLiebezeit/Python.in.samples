import xlwings as xw

try:
    # Excel-Datei öffnen
    wb = xw.Book('C:\\Users\\Falk\\TestData\\TestZahlen.xlsx')
    sheet = wb.sheets['Data']

    """
    # Werte auslesen und bereinigen
    #data = sheet.range('C36:C36').value

  
    #data = [x for x in data if isinstance(x, (int, float))]  # Nur numerische Werte übernehmen
    
    # Berechnungen durchführen
    data_squared = [x + x for x in data]
   
    # Ergebnisse zurückschreiben
    sheet.range('C36:C36+len(data_squared)-1').value = [[x] for x in data_squared]

    # Speichern und schließen
    wb.save()
    wb.close()
    """

    # Wert aus Zelle C36 auslesen
    wert_C36 = sheet.range('C36').value

    # Wert ausgeben
    print(f"Wert in C36: {wert_C36}")

    
    print("Berechnung erfolgreich abgeschlossen!")


except Exception as e:
    print(f"Fehler aufgetreten: {e}")

