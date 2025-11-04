#L_06_05.py
#Kugelvolumen,Kugekoberfläche als Rotationskörper
import numpy as np
import scipy.integrate as integral
from numdifftools import Derivative
r=1
def f(x):
    return np.sqrt(r**2-x**2)
#Funktion quadrieren
def f2(x):
    return f(x)**2

def m(x):
    df=Derivative(f)
    return f(x)*np.sqrt(1+df(x)**2)

#Grenzen
a=-r
b=r
#Volumen
V1=4/3*r**3*np.pi #genau
V2=np.pi*integral.quad(f2,a,b)[0]
#Oberfläche
O1=4*np.pi*r**2 #genau
O2=2*np.pi*integral.quad(m,a,b)[0]
print("-------------Volumen--------")
print("Kugelvolumen genau     :",V1)
print("Kugelvolumen integriert:",V2)
print("absoluter Fehler:       ",V1-V2)
print("-------------Oberfläche-----")
print("Kugeloberfläche genau     :",O1)
print("Kugeloberfläche integriert:",O2)
print("absoluter Fehler:          ",O1-O2)

