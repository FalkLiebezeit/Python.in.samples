#14_rotations_integral.py
import numpy as np
import scipy.integrate as integral
from numdifftools import Derivative
#Funktionsdefinition
def f(x):
    #return x
    return np.sqrt(x)
#Funktion f(x) quadrieren
def f2(x):
    return f(x)**2
#für Mantelfläche
def m(x):
    df=Derivative(f)
    return f(x)*np.sqrt(1+df(x)**2)
#Grenzen
a,b=0,1
V=np.pi*integral.quad(f2,a,b)[0]  #Volumen
M=2*np.pi*integral.quad(m,a,b)[0] #Mantelfläche
print("Volumen      %3.6f VE" %V)
print("Mantelfläche %3.6f FE" %M)

