#13_kettenlinie.py
import numpy as np
import scipy.integrate as integral
from numdifftools import Derivative
a=10 #Krümmumgsradius
def k(x):
    return a*np.cosh(x/a)
#Länge berechnen
def dl(x):
    df=Derivative(k)
    return np.sqrt(1+df(x)**2)
#Abstände
x1,x2=-10,10
laenge=integral.quad(dl,x1,x2)[0]
print("Länge der Kettenlinie %3.2f m" %laenge)
