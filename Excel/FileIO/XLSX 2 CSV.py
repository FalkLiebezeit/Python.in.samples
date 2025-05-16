import pandas as pd


# Datei laden (Pfad anpassen)

input_datei_pfad = "C:\\Users\\Falk\\TestData\\InputData.xlsx"

df = pd.read_excel(input_datei_pfad)



# Inhalt anzeigen
#print(df.head())  # Zeigt die ersten 5 Zeilen der Tabelle

# Inhalt anzeigen
print(df.all)  
print("\n")


# Aktualisiertes DataFrame speichern
output_datei_pfad = "C:\\Users\\Falk\\TestData\\OutputData.csv"

df.to_csv(output_datei_pfad, index=False)
