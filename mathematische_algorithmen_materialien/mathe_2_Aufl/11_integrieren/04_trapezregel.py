#04_trapez.py
from math import *
#Funktionsdefinition
def f(x):
    return x**2 #x**3,x**4,sin(x),exp(x)
#Stammfunktion
def F(x):
    return x**3/3 #x**4/4,x**5/5,-cos(x),exp(x)
#Trapezsummen
def trapez(f,a,b,n=10):
    h=(b-a)/n
    summe=0
    for i in range(1,n):
        summe=summe+f(a+i*h)
    return (summe + (f(a)+f(b))/2)*h
#Grenzen
a,b=0,10
n=10
Aa=trapez(f,a,b,n)
Ag=F(b)-F(a)
#Ausgabe
print("Grenzen: a =",a,"\t b =",b)
print("Anzahl der Zerlegungen n =",n)
print("Schrittweite h =",(b-a)/n)
print("Aa =",round(Aa,6), " approximiert")
print("Ag =",round(Ag,6), " genau")
print("Fehler E =",round(fabs(Ag-Aa),6))

