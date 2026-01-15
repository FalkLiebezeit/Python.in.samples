#L_06_03.py
from sympy import *
a11,a12,a13=symbols('a11,a12,a13')
a21,a22,a23=symbols('a21,a22,a23')
a31,a32,a33=symbols('a31,a32,a33')
#Koeffizientenmatrix
A=Matrix([[a11,a12,a13],
          [a21,a22,a23],
          [a31,a32,a33]])
#Ausgabe
print(A)
print("inverse Matrix\n",A.inv())
