#10_sympy_grenzwert.py
from sympy import *
n=symbols('n')
an=5*(1-1/(2**n))
ga=limit(an,n,oo)
print("Grenzwert von %s ist %3.2f" %(an,ga))