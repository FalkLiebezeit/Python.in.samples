#09_sympy_grenzwert_pi.py
from sympy import *
n=symbols('n')
an=(-1)**(n+1)/(2*n-1)
s=Sum(an,(n,1,oo)).doit()
print("Grenzwert.......:",s)