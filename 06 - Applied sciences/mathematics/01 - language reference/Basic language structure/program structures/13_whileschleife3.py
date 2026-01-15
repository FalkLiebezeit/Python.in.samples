#13_whileschleife3.py
import math as m
def f(x):
    return x-m.cos(x)

eps=1e-12
x1=0
x2=1
n=0
f1=f(x1)
while abs(x2-x1)>eps and n<100:
    n+=1
    x0=x1
    x1=x2
    f0=f1
    f1=f(x1)
    if abs((f1-f0))<eps: break 
    x2=x1-f1*(x1-x0)/(f1-f0)
    print(n,":", x2)
