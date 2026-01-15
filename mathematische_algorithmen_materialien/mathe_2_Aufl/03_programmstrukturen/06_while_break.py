#06_while_schleife3.py
from math import *
print("Berechnung mit x beenden!")
while True:
    eingabe=input("Term eingeben: ")
    if eingabe=='x':break
    try:
        auswertung=eval(eingabe)
    except:
        print("Falsche Eingabe: Programmende")
        break
    print(auswertung)

#help('math') 
   