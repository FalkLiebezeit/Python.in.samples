#17_kettenbruch2.py
from sympy import *
#from sympy.ntheory.continued_fraction import continued_fraction_periodic
z=37 #Zähler
n=14 #Nenner
#Kettenbruch berechnen
kb=continued_fraction_periodic(z,n)
#Bruch berechnen
bruch=continued_fraction_reduce(kb)
#Ausgabe
print("Koeffizienten:",kb)
print("Bruch:",bruch)