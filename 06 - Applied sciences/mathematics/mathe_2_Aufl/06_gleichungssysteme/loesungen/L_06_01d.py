#L_06_01c.py
from sympy import *
a,b,c,d=symbols('a b c d')
A = Matrix([[5, 4, 3, 2],
            [1, 7, 1, 3],
            [2, 1, 11, 1],
            [7, 3, 1, 13]],dtype=float)
b = Matrix([10, 8, 6, 4],dtype=float)
#L=linsolve([A,b],(a,b,c,d)) #01c keine Lösung
L=A.gauss_jordan_solve(b)
print("Lösungsvektor\n",L)
print(N(L[0],9))