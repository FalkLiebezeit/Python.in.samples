#L_07_05.py
from sympy import *
n=symbols('n')
x=0.5
#Folgen
an=2**(1/n)
bn=(1/2)**(1/n)
cn=(1-x**n)**(1/n)
#Grenzwerte berechnen
ga=limit(an,n,oo)
gb=limit(bn,n,oo)
gc=limit(cn,n,oo)
#Ausgabe
print("Grenzwert von %s ist %3.2f" %(an,ga))
print("Grenzwert von %s ist %3.2f" %(bn,gb))
print("Grenzwert von %s ist %3.2f" %(cn,gc))

