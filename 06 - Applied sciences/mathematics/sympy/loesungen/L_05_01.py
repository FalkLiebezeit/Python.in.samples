#L_05_01.py
from sympy import *
x=symbols("x")
y=3*x**4+6*x**2+3+3*x**4+3*x**2+3*x**2+3-6*x**4-6*x**2+2*x**2+2-8*x**2
ys=simplify(y)
print(y)
print(ys)