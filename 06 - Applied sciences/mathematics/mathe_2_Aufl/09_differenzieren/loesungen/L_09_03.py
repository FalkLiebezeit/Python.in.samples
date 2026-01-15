#L_09_03.py
#Mehrfachableitung Hyperbel
from math import *
from numdifftools import Derivative
#Funktionsdefinition
def f(x):
    return 1/x
#Berechnung der Ableitungen
n=10 #Ordnung der Ableitung
x0=2 #Stelle der Steigung
for i in range(1,n+1):
    y1_ = Derivative(f,n=i)
    y2_=(-1)**i*factorial(i)/x0**(i+1)
    print(i,":",y1_(x0)," ",y2_)