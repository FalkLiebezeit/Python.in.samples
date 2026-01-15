#06_sierpinski_sympy.py
from sympy import *
a,n=symbols('a, n')
ln=(3/2)**n
An=sqrt(3)/4*(3/4)**n*a**2
gL=limit(ln,n,oo)
gA=limit(An,n,oo)
print("Sierpinski-Dreieck")
print("Grenzwert der Längen:",gL)
print("Grenzwert der Fläche:",gA)