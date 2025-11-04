#07_matrix_mul1.py
from sympy import *
a,b,c,d = symbols("a,b,c,d")
e,f,g,h = symbols("e,f,g,h")
A=Matrix([[a,b],
          [c,d]])
B=Matrix([[e,f],
          [g,h]])
C=A*B
D=B*A
print("Produkt A*B\n")
pprint(C)
print("\nProdukt B*A\n")
pprint(D)
