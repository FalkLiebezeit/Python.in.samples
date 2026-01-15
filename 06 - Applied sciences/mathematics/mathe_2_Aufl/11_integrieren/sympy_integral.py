from sympy import *
x=symbols('x')
a,b=symbols('a,b')
#f=2
#f=x**2
#f=sin(x)
f=exp(x)
#f=sin(x**2)
#f=sqrt(x)*exp(x)
#f=exp(x**2)
a,b=1,2
F=integrate(f,(x,a,b))

print(F)