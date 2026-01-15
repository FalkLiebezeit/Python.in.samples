#05_simpson.py
from math import *
#Funktionsdefinition
def f(x):
    return x**4 #x**3,x**4,sin(x),exp(x)
#Stammfunktion
def F(x):
    return x**5/5 #x**4/4,x**5/5,-cos(x),exp(x)
#Simpson-Regel
def simpson(f,a,b,n=10):
    h=(b-a)/n
    summe=0
    for i in range(0,n):
        summe = summe + f(a+i*h) + 4*f(a+h/2+i*h) + f(a+(i+1)*h)
    return h*summe/6
#Grenzen
a,b=0,10
n=10
Aa=simpson(f,a,b,n) #approximiert
Ag=F(b)-F(a) #genau
#Ausgabe
print("Grenzen: a =",a,"\t b =",b)
print("Anzahl der Zerlegungen n =",n)
print("Schrittweite h =",(b-a)/n)
print("Aa =",Aa," approximiert")
print("Ag =",Ag, " genau")
print("Fehler E =",fabs(Ag-Aa))

'''
#ander Varianten
#Variante 2: nur zwei Summen
def simpson2(f,a,b,n=100):
    h=(b-a)/(2*n)
    su=sg=summe=0
    for i in range(0,n):
            su=su + 4*f(a+(2*i+1)*h)
    for i in range(1,n):
            sg=sg + 2*f(a+2*i*h)
    summe = summe + f(a) + f(b) + su + sg
    return h*summe/3
#Variante 3: nur zwei Summen, aber in einer Schleife
def simpson3(f,a,b,n=100):
    n=2*n
    h=(b-a)/n
    su=sg=summe=0
    for i in range(1,n):
        if i%2==0: #gerade
            sg=sg + f(a+i*h)
        else:      #ungerade
            su=su + f(a+i*h)
    summe = summe + f(a) + f(b) + 4*su + 2*sg
    return h*summe/3

'''


