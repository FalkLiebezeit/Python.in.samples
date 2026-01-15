#14_funktion1.py
#erste Funktionsdefinition
def addition(a,b):
    return a+b
#zweite Funktionsdefinition
def multiplikation(a,b):
    return a*b
#Vorgabe der Werte
a1,b1=11,42
#Funktionsaufrufe
summe=addition(a1,b1)
produkt=multiplikation(a1,b1)
#Ausgabe
print("a1 =",a1,"b1 =",b1)
print("Addition:",summe)
print("Multiplikation:",produkt)