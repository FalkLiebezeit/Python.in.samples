#08_rotationskoerper.py
from math import *
from integrieren import *
from scipy.integrate import quad
#Wurzelfunktion
def f(x):
    return sqrt(x)
#Quadrat der Wurzelfunktion
def f2(x):
    return f(x)**2
#1. Ableitung
def diff(f,x,h=1e-6):
    return (f(x+h)-f(x-h))/(2*h)
#Abschnitt der Mantelfläche
def diffM(x):
    return f(x)*sqrt((1+(diff(f,x))**2))
#Hauptprogramm
a,b=1,5  #Grenzen
V=pi*simpson(f2,a,b,100)      #Volumen
M=2*pi*simpson(diffM,a,b,100) #Mantelfläche
print("Volumen\n",V,"\n",pi*quad(f2,a,b)[0],"quad")
print("Mantelfläche\n",M,"\n",2*pi*quad(diffM,a,b)[0],"quad")


#pi*(21*sqrt(21)-5*sqrt(5))/6
'''
from sympy import *
x=symbols('x')
f=sqrt(x)*sqrt(1+1/(4*x))
F=integrate(f)
V=pi*integrate(f,(x,1,5))
print(F)
print(V)
'''
