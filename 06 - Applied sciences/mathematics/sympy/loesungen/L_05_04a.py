#L_05_04.py
from sympy import *
x,a=symbols("x a")

y1=1/sqrt(a**2-x**2)
y2=x/sqrt(a**2-x**2)
y3=x**2/sqrt(a**2-x**2)
y4=x**3/sqrt(a**2-x**2)
y5=1/(x*sqrt(a**2-x**2))

print(integrate(y1,x))
print(integrate(y2,x))
print(integrate(y3,x))
print(integrate(y4,x))
print(integrate(y5,x))