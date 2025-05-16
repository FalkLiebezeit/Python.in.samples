import pandas as pd

# Datei öffnen oder erstellen
datei = "C:\\Users\\Falk\\TestData\\CreateRows 2.xlsx"

# Eine Liste mit 10 Zahlen erstellen
zahlen = list(range(1, 11))

# Einen DataFrame mit mindestens 1 Zeile und 3 Spalten erstellen
df = pd.DataFrame(index=range(1), columns=["A", "B", "C"]) 

# Zahlen in Spalte C (Index 3) schreiben
for i, zahl in enumerate(zahlen, start=1):
    #ws.cell(row=i, column=3, value=zahl)  # Spalte C entspricht Index 3
    df.loc[i, "C"] = zahl  # Beispielwert 42

# Datei speichern
df.to_excel(datei, index=False)

print("Die Werte wurden erfolgreich erstellt und gespeichert!")