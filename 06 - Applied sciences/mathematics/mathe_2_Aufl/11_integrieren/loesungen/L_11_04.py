#L_11_04.py
#Simpson-Regel
from math import *
#
def f(x):
    return 1/x + exp(2*x) + sin(3*x) + log(4*x)
#Simpson-Regel
def simpson(f,a,b,n=100):
    summe=0
    h=(b-a)/n
    for i in range(0,n):
        summe=summe+f(a+i*h)+4*f(a+h/2+i*h)+f(a+(i+1)*h)
    return h*summe/6
#
a,b=1,5
A=simpson(f,a,b)
print(A)
'''
#scipy
from scipy.integrate import quad
A = quad(f,a,b)[0]
print(A)
#sympy
from sympy import *
x=symbols('x')
y = f(x) 
A=integrate(y,(x,1,5))
print(A.evalf(17),"genau")
'''
