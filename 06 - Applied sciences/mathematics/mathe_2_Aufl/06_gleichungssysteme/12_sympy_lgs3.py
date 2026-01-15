#13_sympy_lgs3.py
from sympy import *
x1, x2, x3 = symbols('x1 x2 x3')
b = Matrix([10,14,16])
A = Matrix([[3, 2, 1],
            [1, 2, 3],
            [2, 1, 4]])
Ab=A.col_insert(3,b)
L=solve_linear_system(Ab, x1, x2, x3)
print("Type von solve_linear_system()\n",type(L))
print("Lösungsvektor\n",L)
print(L.keys())
print(L.values())
print("x1 =",L[x1])
print("x2 =",L[x2])
print("x3 =",L[x3])

