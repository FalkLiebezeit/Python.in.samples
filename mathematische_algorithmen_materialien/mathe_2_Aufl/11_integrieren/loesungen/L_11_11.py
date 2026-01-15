#L_11_11.py
#uneigentliches Integral
import numpy as np
from scipy.integrate import quad
#e-Funktion
def f(x):
    return np.exp(-x)
#Berechnung des Integrals
A=quad(f,0,np.inf)[0]
print(A)




