#04_steigung1.py
import numpy as np
from scipy.misc import derivative

def f(x):
    return 0.25*x**2
#zentraler Differenzenquotient
def df(x,h):
    return (f(x+h)-f(x-h))/(2*h)

xs=2   #Stelle der Steigung
h=1e-6 #Genauigkeit
o=3    #ungerade Stützpunkte 
#Sekantensteigung
mS=df(xs,h)
#Tangentensteigung
mT=derivative(f,xs,dx=h,n=1,order=o)
a1=np.degrees(np.arctan(mS))
a2=np.degrees(np.arctan(mT))
print("Sekantensteigung  m=%2.6f %s=%2.1f°"%(mS,chr(945),a1))
print("Tangentensteigung m=%2.6f %s=%2.1f°"%(mT,chr(945),a2))
