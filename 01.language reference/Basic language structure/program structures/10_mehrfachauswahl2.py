#10_mehrfachauswahl2.py
tarif1,tarif2,tarif3=0.3,0.25,0.2
verbrauch=5500 #kWh

if 0 < verbrauch <= 5000:
    print("Betrag für Tarif1:",verbrauch*tarif1,"Euro")
elif 5000 < verbrauch <= 10000:
    print("Betrag für Tarif2:",verbrauch*tarif2,"Euro")
elif 10000 < verbrauch <= 30000:
    print("Betrag für Tarif3:",verbrauch*tarif3,"Euro")
else:
    print("Industrietarif!")

    