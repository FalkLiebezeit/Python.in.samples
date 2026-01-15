#09_zweifach_integral.py
from math import *
from scipy.integrate import dblquad
#Funktionsdefinition
def f(x,y):
    return 5-x-y #x**2+y,x*exp(y),exp(-(x**2+y**2))
#Zweifachintegral
def zweifach(f,y1,y2,x1,x2,n=200,m=200):
    dx=(x2-x1)/n
    dy=(y2-y1)/m
    sy=0
    for i in range(n):
        y=y1+i*dy+dy/2
        sx=0
        for j in range(m):
            x=x1+j*dx+dx/2
            sx=sx+f(x,y)
        sy=sy+sx
    return sy*dx*dy
#Grenzen der x-Achse
x1,x2=0,2
#Grenzen der y-Achse
y1,y2=0,1
V1=zweifach(f,y1,y2,x1,x2)
V2= dblquad(f,y1,y2,x1,x2)[0]
print("Volumen:",V1)
print("Volumen:",V2,"dblquad")

