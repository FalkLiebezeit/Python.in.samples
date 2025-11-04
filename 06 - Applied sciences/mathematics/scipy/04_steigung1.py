#04_steigung1.py
import numpy as np
from numdifftools import Derivative
#Funktion
def f(x):
    return 0.25*x**2
#zentraler Differenzenquotient
def df(x,h):
    return (f(x+h)-f(x-h))/(2*h)

xs=2   #Stelle der Steigung
h=1e-6 #Genauigkeit
mS=df(xs,h) #Sekantensteigung
mT=Derivative(f,n=1) #Tangentensteigung
a1=np.degrees(np.arctan(mS))
a2=np.degrees(np.arctan(mT(xs)))
print("Sekantensteigung  m=%2.6f %s=%2.1f°"%(mS,chr(945),a1))
print("Tangentensteigung m=%2.6f %s=%2.1f°"%(mT(xs),chr(945),a2))
'''
Das Modul numdifftools muss installiert werden:
pip install numdifftools
'''
