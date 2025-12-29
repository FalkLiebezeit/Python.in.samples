#L_06_04.py
#Kreisumfang
import numpy as np
import scipy.integrate as integral
from numdifftools import Derivative
r=1  #Radius
#r=wurzel(x^2+y^2)
def f(x):
    return np.sqrt(r**2-x**2)
'''
#selbstdefinierte Funktion zum testen
def derivative(f,x,h=1e-9):
    return (f(x+h)-f(x-h))/(2.0*h)

def dl(x):
    return np.sqrt(1.0+derivative(f,x)**2)
'''
#numdifftools
def dl(x): 
    df=Derivative(f,method='complex')
    return np.sqrt(1.0+df(x)**2)

#Abstände
a=-r
b=r
#Kreisumpfang
U1=2.0*r*np.pi #genau
U2=2.0*integral.quad(dl,a,b)[0]
print("Kreisumfang genau:     ",U1)
print("Kreisumfang integriert:",U2)
print("absoluter Fehler:      ",U1-U2)
