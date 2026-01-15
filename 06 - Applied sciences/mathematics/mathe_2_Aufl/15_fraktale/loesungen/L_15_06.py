#L_15_06.py
from sympy import *
a,n=symbols('a n')
#Höhe
h=2*a*Sum((1/2)**n,(n,0,oo)).doit()
print("Symmetrischer Pythagoras-Baum")
print("Höhe:",h)
