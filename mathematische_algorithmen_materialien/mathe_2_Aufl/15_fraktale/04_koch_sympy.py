#04_koch_sympy.py
from sympy import *
a,n=symbols('a, n')
Un=3*(4/3)**n
An=sqrt(3)*a**2/4*(1+3/4*Sum((4/9)**n,(n,1,oo)).doit())
gU=limit(Un,n,oo)
gA=limit(An,n,oo)
print("Koch'sche Schneeflocke")
print("Grenzwert der Länge:",gU)
print("Flächeninhalt der Schneeflocke:",An)
print("Grenzwert der Fläche          :",gA)

