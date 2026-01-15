#07_sympy_grenzwert_e.py
from sympy import *
k,n=symbols('k n')
ak=1/factorial(k)
sn=Sum(ak,(k, 0, n)).doit()
g=limit(sn,n,oo)
s=Sum(ak,(k,0,oo)).doit()
print("Grenzwert der Partialsumme:",g)
print("Unendliche Summe..........:",s)