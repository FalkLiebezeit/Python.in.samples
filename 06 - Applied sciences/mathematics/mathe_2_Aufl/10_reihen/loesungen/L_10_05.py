#L_10_05.py
from sympy import *
x=symbols('x')
f=1/(1-x)
print("1/(1-x)=",series(f,x,n=10))