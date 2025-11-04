#L_06_02.py
#Laenge einer log. Spirale
import numpy as np
import scipy.integrate as integral
from numdifftools import Derivative
a=0.1  
b=0.5
#x ist eine Winkel
def r(x):
    return a*np.exp(b*x)

def dl(x): 
    df=Derivative(r,method='complex')
    return np.sqrt(r(x)**2 + df(x)**2)
#Abstände
phi1=0
phi2=2*np.pi
#Laenge der Spirale
lg=np.sqrt(b**2+1)/b*(r(phi2)-r(phi1))#genau
li=integral.quad(dl,phi1,phi2)[0]     #integriert
print("Laenge einer logarithmischen Spirale")
print("genau:      ",lg)
print("integriert: ",li)
print("absoluter Fehler:",lg-li)


