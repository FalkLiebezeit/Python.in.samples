#21_o_notation.py
from sympy import *
n=symbols('n')
f=2*n**3-n**2
g=n**3
schranke=limit(f/g,n,oo)
print("obere Schranke:",schranke)
O_n=O(f,(n,oo)),f in O(g,(n,oo))
print(f,"\nist von der Ordnung ", O_n[0])
print(O_n[1])

