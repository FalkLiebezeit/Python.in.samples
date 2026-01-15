#L_08_08.py
#Newton-Verfahren as Funktion
from math import *
from scipy import optimize
#Testfunktionen
def f(x):
    y = x-cos(x)           #a)
    #y = x**2-sin(x)        #b)
    #y = exp(x)- x**2/4 - 2  #c)
    #y = log(x+2)-2*x**2     #d)
    return y
#Newton-Verfahren
def newton(f,x,eps=1e-12,h=1e-4):
    x0=f(x)
    n=0
    while fabs(x0-x)>eps and n < 100:
        x0=x  
        x = x - 2*h*f(x)/(f(x+h)-f(x-h))
        n=n+1
    return x
#Hauptprogramm
x0=0.5
print(newton(f,x0))
print(optimize.newton(f,x0),"scipy")




