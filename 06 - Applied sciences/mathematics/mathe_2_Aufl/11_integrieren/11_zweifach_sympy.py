#11_zweifach_sympy.py
from sympy import *
x,y =symbols('x y')
z=x+y**2
x1,x2=0,1-y/2
y1,y2=0,2
print("Zweifachintegral von z =",z)
print("in den inneren Grenzen von",x1,"bis",x2)
print("in den äußeren Grenzen von",y1,"bis",y2)
V=integrate(z, (x, x1, x2), (y, y1, y2))
print("Volumen V =",V)


# y=sin(x)/x
# #y=sin(x**2)
# #y=sqrt(x**3+1)
# #y=exp(-x**2)
# #y=(x**2+1)**(1/3)
# #y=sqrt(x)*exp(x)
# integral=integrate(y,x)
# print(integral)
