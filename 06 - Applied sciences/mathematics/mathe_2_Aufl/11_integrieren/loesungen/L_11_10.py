#L_11_10.py
from math import *
from scipy.integrate import quad
#Funktionsdefinition
def f(x):
#     return sin(x**3)
#     return sqrt(x**3+1)
#     return (x**1+1)**(1/3)
    return sqrt(x)*exp(x)
#
a,b=1,2
A=quad(f,a,b)[0]
print(A)

