#07_bogenlaenge.py
from math import *
from integrieren import *
from scipy.integrate import quad
#Normalparabel
def f(x):
    return x**2
#1. Ableitung
def diff(f,x,h=1e-3):
    return (f(x+h)-f(x-h))/(2*h)
#Abschitt der Bogenlänge
def dbl(x):
    return sqrt(1+(diff(f,x))**2)
#Hauptprogramm
a,b=0,1  #Grenzen
s=simpson(dbl,a,b,100)
print("Bogenlänge einer Normalparabel")
print(s)
print(quad(dbl,a,b)[0],"quad")
print(sqrt(5)/2+log(2+sqrt(5))/4,"genau")