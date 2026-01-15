#17_sympy_euler.py
from sympy import *
x=symbols('x')

r1=series(cos(x),n=8)
r2=series(I*sin(x),n=8)
r3=series(exp(I*x),n=6)
r4=series(cos(x)+I*sin(x),n=6)
#r4=r1+r2
print("eulersche Formel")
print("cos(x)\t\t=",r1)
print("i*sin(x)\t=",r2)
print("exp(i*x)\t=",r3)
print("cos(x)+i*sin(x) =",r4)