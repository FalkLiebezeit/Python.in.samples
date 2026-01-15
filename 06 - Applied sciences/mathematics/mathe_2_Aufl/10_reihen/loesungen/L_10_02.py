#05_sympy_grenzwert.py
from sympy import *
n=symbols('n')
an=1/n**2
s=Sum(an,(n, 1, oo)).doit()
g=limit(s,n,oo)
print("unendliche Summe:",s)
print("Grenzwert.......:",g)