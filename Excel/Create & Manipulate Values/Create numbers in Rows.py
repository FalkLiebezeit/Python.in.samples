import pandas as pd
from openpyxl import Workbook


# Eine Liste mit 10 Zahlen erstellen
zahlen = list(range(1, 11))

# Eine neue Excel-Arbeitsmappe erstellen
wb = Workbook()
ws = wb.active

# Zahlen in Spalte C (Index 3) schreiben
for i, zahl in enumerate(zahlen, start=1):
    ws.cell(row=i, column=3, value=zahl)  # Spalte C entspricht Index 3

# Datei speichern
datei = "C:\\Users\\Falk\\TestData\\CreateRows.xlsx"

wb.save(datei)

print(f"Die Datei '{datei}' wurde erfolgreich erstellt mit den Zahlen in Spalte C!")

    


  
