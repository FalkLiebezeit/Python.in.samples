#L_11_03.py
from math import *
#Funktionsdefinition
def f(x):
    return x**2 #x**3,x**4,sin(x),exp(x)
#Stammfunktion
def F(x):
    return x**3/3 #x**4/4,x**5/5,-cos(x),exp(x)
#Rechtecksummen
def untersumme(f,a,b,n=10):
    h=(b-a)/n
    summe=0
    for i in range(0,n):
        summe=summe+f(a+i*h)
    return h*summe
#Obersumme
def obersumme(f,a,b,n=10):
    h=(b-a)/n
    summe=0
    for i in range(1,n+1):
        summe=summe+f(a+i*h)
    return h*summe
#Grenzen
a,b=0,10
n=10
Au=untersumme(f,a,b,n) #approximiert
Ao=obersumme(f,a,b,n) #approximiert
Am=(Au+Ao)/2 #Mittelwert
Ag=F(b)-F(a) #genau
#Ausgabe
print("Grenzen: a =",a,"\t b =",b)
print("Anzahl der Zerlegungen n =",n)
print("Schrittweite h =",(b-a)/n)
print("Au =",round(Au,6), " Untersumme")
print("Ao =",round(Ao,6), " Obersumme")
print("Am =",Am,"Mittelwert")
print("Ag =",round(Ag,6), " genau")
#print("Fehler E =",round(fabs(Ag-Aa),6))

'''
from sympy import *
x=symbols('x')
y=sin(x)
print(integrate(y))
'''

