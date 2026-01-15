#L_11_06.py
from math import *
import simpson as sim
from scipy.integrate import quad
#
def f(x):
    return cosh(2*x)
#
a,b=1,5
As=sim.simpson(f,a,b,100)
Aq = quad(f,a,b)[0]
print(As)
print(Aq)

'''
from sympy import *
x=symbols('x')
y=cosh(2*x)
a,b=1,5
A=integrate(y,(x,a,b))
print(A)
print(N(A,6))
'''