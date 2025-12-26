#16_kettenbruch1.py
from sympy import *
z=37 #Zähler
n=14 #Nenner
#Kettenbruch berechnen
def kb(z,n):
    r=[]
    while n>0:
        r.append(z//n)  
        z=z%n
        z,n=n,z
    return r
#Umwandlung in Bruch
def ikb(ls):
    a = Integer(0)
    for i in reversed(ls[1:]):
        a=a+i
        a=1/a
    return ls[0] + a
#berechnet Kettenbruch
kb1=kb(z,n)
#berechnet Bruch
ikb1=ikb(kb1)
#Ausgabe
print("Koeffizienten:",kb1)
print("Bruch:",ikb1)

     