#08_matrix_mul2.py
from sympy import *
s,L1,C2,L3,C4,L5 = symbols("s L1 C2 L3 C4 L5")
A1=Matrix([[1,s*L1],
           [0, 1]])
A2=Matrix([[1,  0],
           [C2*s,1]])
A3=Matrix([[1,L3*s],
           [0, 1]])
A4=Matrix([[1,   0],
           [C4*s, 1]])
A5=Matrix([[1,L5*s],
           [0,   1]])
A6=Matrix([[1, 0],
           [1, 1]])
A=A1*A2*A3*A4*A5*A6
print("Kettenparameter")
print(A)
print("Nennerpolynom der Übertragungsfunktion")
print(expand(A[0,0]))