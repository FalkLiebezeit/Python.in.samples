#15_funktion2.py
def berechnung(a,b):
    '''Die Funktion berechnet die Summe
       und das Produkt aus zwei Zahlen.'''
    s=a+b
    p=a*b
    return (s,p)
    #return [s,p]
#Vorgabe der Werte
a1,b1=11,42
#Funktionsaufruf
summe,produkt = berechnung(a1,b1)
#Ausgabe
print("a1 =",a1,"b1 =",b1)
print("Summe:",summe)
print("Multiplikation:",produkt)


    
    

