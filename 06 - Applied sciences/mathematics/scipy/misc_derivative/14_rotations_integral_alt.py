#14_rotations_integral_alt.py
import numpy as np
import scipy.integrate as integral
from scipy.misc import derivative

def f(x):
    #return x
    return np.sqrt(x)

def f2(x):
    return f(x)**2

def m(x):
    return f(x)*np.sqrt(1+derivative(f,x,dx=1e-6)**2)

#Grenzen
a=0
b=1
#Volumen
V=np.pi*integral.quad(f2,a,b)[0]
#Mantelfläche
M=2*np.pi*integral.quad(m,a,b)[0]
print("Volumen      %3.6f VE" %V)
print("Mantelfläche %3.6f FE" %M)
