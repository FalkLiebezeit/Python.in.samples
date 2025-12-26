#18_grenzwert1.py
from sympy import *
n=symbols("n")
#Folgen
a1=2*n
a2=n**2
a3=1/n
a4=(2*n**3+2)/(n**3+n**2-5)
a5=(1+1/n)**n
#Ausgabe
print("Grenzwerte für n gegen ∞")
print("Grenzwert von %s ist: %s" %(a1,limit(a1,n,oo)))
print("Grenzwert von %s ist: %s" %(a2,limit(a2,n,oo)))
print("Grenzwert von %s ist: %s" %(a3,limit(a3,n,oo)))
print("Grenzwert von %s ist: %s" %(a4,limit(a4,n,oo)))
print("Grenzwert von %s ist: %s" %(a5,limit(a5,n,oo)))