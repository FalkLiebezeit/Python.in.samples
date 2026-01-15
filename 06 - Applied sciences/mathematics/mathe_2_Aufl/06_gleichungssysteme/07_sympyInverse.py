#08_sympyInverse.py
from sympy import symbols, Matrix
a,b,c,d=symbols('a,b,c,d')
#Koeffizientenmatrix
A=Matrix([[a,b],
          [c,d]])
#Ausgabe
print(A)
print("inverse Matrix\n",A.inv())
print(type(Matrix))
