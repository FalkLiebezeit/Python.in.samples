#L_05_02.py
#Grenzwerte
from sympy import *
x,n=symbols("x n")
ya=sin(n*x)/x
yb=tan(n*x)/x
yc=sin(x)/(x*pow(cos(x),1/3))
yd=(sin(2*x)-2*sin(x))/(2*E**x-x**2-2*x-2)
print(limit(ya,x,0))
print(limit(yb,x,0))
print(limit(yc,x,0))
print(limit(yd,x,0))