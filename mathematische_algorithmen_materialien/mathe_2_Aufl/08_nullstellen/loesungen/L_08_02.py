#L_08_02.py
#Bisektion mit for-Schleife
from math import *
def f(x):
    return x**2 - 2
#Hauptprogramm
k=6
eps=10**-k 
a=0
b=2
n=int(log2(b-a) + k*log2(10)+1)
for n in range(n):
    x=(a+b)/2
    if f(x)*f(a)<0:
        b=x
    else:
        a=x
    print(x)
#
print(sqrt(2),"genau")
print(n)
    
