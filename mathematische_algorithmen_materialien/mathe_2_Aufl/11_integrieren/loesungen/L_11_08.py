#L_11_08.py
#Rotationskörper
import numpy as np
from scipy.integrate import quad
#f für Rotationskörper
def f(x):
    return (x-5)**2+5
#f(x) quadrieren
def f2(x):
    return f(x)**2
#1. Ableitung
def derivative(f,x,h=1e-6):
    return (f(x+h)-f(x-h))/(2*h)
#
def dm(x):
    return f(x)*np.sqrt(1+derivative(f,x)**2)
#Hauptprogramm
a,b=2,5 #Grenzen der x-Achse
x=np.linspace(a,b,100)
V=  np.pi*quad(f2,a,b)[0]
M=2*np.pi*quad(dm,a,b)[0]
print("Volumen     :",V)
print("Mantelfläche:",M)