#L_05_04.py
from sympy import *
x,a,b,n=symbols("x a b n")

y1=exp(a*x)
y2=x**2*exp(x)*cos(x)
y3=1/(1+cos(x))
y4=tan(x)
y5=sin(x)*cos(x)

print(integrate(y1,x))
print(integrate(y2,x))
print(integrate(y3,x))
print(integrate(y4,x))
print(integrate(y5,x))