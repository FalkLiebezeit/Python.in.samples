#L_05_03.py
from sympy import *
x,a,b=symbols("x a b")
y1=sin(a*x)*cos(b*x)
y2=sin(a*x)/cos(b*x)
y3=(x**3+2*x)/(4*x**2-7)
y4=pow(1-cos(x)**4*x,2)
y5=atan(x)
print(diff(y1,x))
print(diff(y2,x))
print(diff(y3,x))
print(diff(y4,x))
print(diff(y5,x))