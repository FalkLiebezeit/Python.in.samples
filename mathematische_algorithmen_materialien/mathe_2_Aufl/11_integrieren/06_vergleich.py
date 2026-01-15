#06_vergleich.py
from math import *
from integrieren import *
from scipy.integrate import quad
#Funktionsdefinition
def f(x):
    #y=x**2
    #y=x**4
    #y=sin(x)
    y=1/x
    return y
#Hauptprogramm
a,b=1,2 #Grenzen
n=20
A1=rechteck(f,a,b,n)
A2=trapez(f,a,b,n)
A3=simpson(f,a,b,n)
A4=quad(f,a,b) [0]
#Ausgaben
print("Grenzen: a =",a,"\t b =",b)
print("Anzahl der Zerlegungen n =",n)
print(A1,"Rechtecksummen")
print(A2,"Trapezsummen")
print(A3,"Simpson")
print(A4,"quad")
print(log(2),"genau")

   

