#L_08_01.py
from math import *
def f(x):
    return x**2 - 2 
#Hauptprogramm
eps=1e-6
a=0
b=2
n=0
print("%3s %8s %10s %14s %12s %14s %10s"%("n","a","x","b","f(a)","f(x)","f(b)"))
while abs(a-b)>eps:
    x=(a+b)/2
    if f(x)*f(a)<0:
        b=x
    else:
        a=x
    n=n+1
    print(" %2d  %.9f  %.9f  %.9f %.9f %+0.9f %.9f" %(n,a,x,b,f(a),f(x),f(b)))


