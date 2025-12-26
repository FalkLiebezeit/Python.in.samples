#13_kettenlinie_alt.py
import numpy as np
import scipy.integrate as integral
from scipy.misc import derivative
a=10 #Krümmumgsradius
def k(x):
    return a*np.cosh(x/a)

def dl(x):
    return np.sqrt(1+derivative(k,x,dx=1e-6)**2)
#Abstände
x1=-10
x2=10
#Bogenlänge
laenge=integral.quad(dl,x1,x2)[0]
print("Länge der Kettenlinie %3.2f m" %laenge)