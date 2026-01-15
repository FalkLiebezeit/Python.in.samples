#L_06_02.py
from sympy import *
a11, a12 =symbols('a11, a12')
a21, a22 =symbols('a21, a22')
x1, x2 =symbols('x1, x2')
b1, b2 =symbols('b1, b2')
A=Matrix([[a11, a12],
          [a21, a22]])
b=Matrix([b1,b2])
L=linsolve([A,b],(x1,x2))
D=A.det()
print("Lösungsvektor\n",L)
print("Systemdeterminante\n D =",D)
print(A.inv())




