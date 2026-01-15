#08_sympy_analysis.py
from sympy import *
x = symbols('x')
f=-x**2+5*x-3
df=diff(f,x,1)
F=integrate(f,x)
L=solve(f,x)
A=integrate(f,(x,L[0],L[1]))
print("Polynom       f(x) =",f)
print("1. Ableitung f'(x) =",df)
print("Stammfunktion F(x) =",F)
print("Nullstellen:  ",L)
print("Flächeninhalt:",N(A,16))

