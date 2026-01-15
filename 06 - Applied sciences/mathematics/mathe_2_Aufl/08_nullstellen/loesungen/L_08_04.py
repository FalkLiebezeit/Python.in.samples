#L_08_04.py
#Bisektionsverfahren mit Funktion
from math import *
from scipy.optimize import newton
#Testfunktionen
def f(x):
    #y = x-cos(x)           #a)
    #y = x**2-sin(x)        #b)
    y = exp(x)- x**2/4 - 2  #c)
    #y = log(x+2)-2*x**2     #d)
    return y
#Bisektionsverfahren
def  bisektion(f,a,b,eps=1e-12):
    while abs(a-b)>eps:
        x=(a+b)/2
        if f(x)*f(a)<0:
            b=x
        else:
            a=x
    return x
#Hauptprogramm
a=0
b=1
print(bisektion(f,a,b))
print(newton(f,b),"scipy")