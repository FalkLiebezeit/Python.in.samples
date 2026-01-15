#L_10_04.py
from sympy import *
n=symbols('n')

def a(n):
    return 2**n/factorial(n)
    
R=limit(abs(a(n)/a(n+1)),n,oo)
print("Konvergenzradius:",R)