#04_quersumme.py
#Division mit Rest
def quersumme1(z):
    qs=0
    while z!=0:
        qs=qs+z%10
        z=z//10
    return qs
#typische Lösung mit Python
def quersumme2(z):
    strZahl=str(z)
    qs=0
    for ziffer in strZahl:
        qs=qs+int(ziffer)
    return qs
#Hauptprogramm
zahl=123456789
#q=quersumme1(zahl)
q=quersumme2(zahl)
print("Die Quersumme von",zahl,"ist",q)

