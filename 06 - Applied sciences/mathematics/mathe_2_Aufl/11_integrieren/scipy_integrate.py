#scipy_integrate.py
import numpy as np
from scipy.integrate import quad,simpson,romberg
n=2
#Funktionsdefinition
def f(x):
    return x**n
#Hauptprogramm
a,b=0,10
x = np.arange(0,11)
y = np.power(x,n)
#numerische Integration
Aq=quad(f,a,b)[0]
Ar=romberg(f,a,b)
As=simpson(y,x)
#Ausgabe
print(Aq,"quad")
print(Ar,"romberg")
print(As,"simpson")
