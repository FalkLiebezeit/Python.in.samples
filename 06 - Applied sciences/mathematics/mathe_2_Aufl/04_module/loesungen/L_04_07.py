#L_04_07.py
from sympy import symbols, Matrix
a11,a12,a13 = symbols('a11,a12,a13')
a21,a22,a23 = symbols('a21,a22,a23')
b11,b12 = symbols('b11,b12')
b21,b22 = symbols('b21,b22')
b31,b32 = symbols('b31,b32')
A=Matrix([[a11,a12,a13],
          [a21,a22,a23]])
B=Matrix([[b11,b12],
          [b21,b22],
          [b31,b32]])
C=A*B
print(C)