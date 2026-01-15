#03_mittelpunktregel.py
from math import *
#Funktionsdefinition
def f(x):
    return x**2 #x**3,x**4,sin(x),exp(x)
#Stammfunktion
def F(x):
    return x**3/3 #x**4/4,x**5/5,-cos(x),exp(x)
#Rechtecksummen
def rechteck(f,a,b,n=10):
    h=(b-a)/n
    summe=0
    for i in range(0,n):
        summe=summe+f(a+i*h+h/2)
    return h*summe
#Grenzen
a,b=0,10
n=10
Aa=rechteck(f,a,b,n) #approximiert
Ag=F(b)-F(a) #genau
#Ausgabe
print("Grenzen: a =",a,"\t b =",b)
print("Anzahl der Zerlegungen n =",n)
print("Schrittweite h =",(b-a)/n)
print("Aa =",round(Aa,6), " approximiert")
print("Ag =",round(Ag,6), " genau")
print("Fehler E =",round(fabs(Ag-Aa),6))




# from sympy import *
# x=symbols('x')
# y=sin(x)
# print(integrate(y))

# from scipy.integrate import quad
# print(quad(f,0,10))

      