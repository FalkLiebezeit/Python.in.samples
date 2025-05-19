import pandas as pd
import os

# Reading CSV files
import csv

df = pd.DataFrame()  # Erstellt ein leeres DataFrame

aktuelles_verzeichnis = os.getcwd()
print(f"Aktuelles Verzeichnis: {aktuelles_verzeichnis}")


# Open the CSV file
#datei_pfad = "C:\\Users\\Falk\\Downloads\\FFB.csv"  # Passe den Pfad an deine Datei an

#with open('C:\\Users\\Falk\\TestData\\FFB.csv', 'r') as file:
with open('.\\Excel\\FileIO\\FFB.csv', 'r') as file:

    # Create a CSV reader object
    csv_reader = csv.reader(file)

    # Iterate over each row in the CSV file
    for row in csv_reader:
        # Each row is a list of values separated by commas
        #print(row)
        # Zeile zum DataFrame hinzufügen
        df=df._append(row, ignore_index=True)





# Aktualisiertes DataFrame speichern
df.to_csv("CSV 2 DF XLSX.csv", index=False)

# Aktualisiertes DataFrame speichern
df.to_excel("CSV 2 DF XLSX.xlsx", index=False)

# Überprüfen, ob die Zeile hinzugefügt wurde
print(df.tail())  # Zeigt die letzten Zeilen des DataFrames
print(df.head)    # Zeigt die ersten Zeilen des DataFrames


