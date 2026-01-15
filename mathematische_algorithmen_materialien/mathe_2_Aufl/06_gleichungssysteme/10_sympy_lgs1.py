#11_sympy_lgs1.py
from sympy import symbols, solve
x1,x2,x3=symbols('x1,x2,x3')
g1= 3*x1+2*x2+  x3-10
g2=   x1+2*x2+3*x3-14
g3= 2*x1+  x2+4*x3-16
L=solve([g1,g2,g3],(x1,x2,x3),dict=True)
print("Lösungsvektor\n",L)
print("Schlüssel\n",L[0].keys())
print("Werte\n",L[0].values())
print("x1 =",L[0][x1])
print("x2 =",L[0][x2])
print("x3 =",L[0][x3])
