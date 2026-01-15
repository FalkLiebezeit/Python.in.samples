#03_newton.py
from math import *
#Funktionsdefinition
def f(x):
    return exp(x/4)-5*x-1
#1. Ableitung
def diff1(x):
    return exp(x/4)/4-5
#2. Ableitung
def diff2(x):
    return exp(x/4)/16
#Hauptprogramm
x=18   #Startwert
eps=1e-6 #;h=1e-4
a,b=17,19
xa=f(x)
n=0
while abs(xa-x)>eps:
    xa=x
    x = x - f(x)/diff1(x) #x=x-2*h*f(x)/(f(x+h)-f(x-h))
    n=n+1
    print(n,"",x)
from scipy.optimize import newton
print("  ",newton(f,18),"scipy")
#Fehlerabschätzung
m=min(abs(diff1(a)),abs(diff1(b)))
M=max(abs(diff2(a)),abs(diff2(b)))
E = 0.5*M*abs(xa-x)**2/m
print("A-posteriori Fehlerabschätzung",E)


# print("Nullstelle\n  ",newton(diff1,x))
   
#12 als Startwert einsetzen, was passiert? Nullstelle!

#Fehlerabschätzung: Königsberger: 293
# from sympy import *
# x=symbols('x')
# f=exp(x/4)-5*x-1
# print(diff(f,x,1))
# print(diff(f,x,2))
