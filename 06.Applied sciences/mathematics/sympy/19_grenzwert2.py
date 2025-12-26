#19_grenzwert.py
from sympy import *
a,x=symbols("a x")
#Funktionen
y1=sin(x)/x
y2=tan(x)/x
y3=a*(1-exp(-x))
y4=1/x+2
y5=(x**2-1)/(x-1)
#Ausgabe
print("Grenzwert von %s gegen 0 ist: %s" %(y1,limit(y1,x,0)))
print("Grenzwert von %s gegen 0 ist: %s" %(y2,limit(y2,x,0)))
print("Grenzwert von %s gegen ∞ ist: %s" %(y3,limit(y3,x,oo)))
print("Grenzwert von %s gegen ∞ ist: %s" %(y4,limit(y4,x,oo)))
print("Grenzwert von %s gegen 1 ist: %s" %(y5,limit(y5,x,1)))
