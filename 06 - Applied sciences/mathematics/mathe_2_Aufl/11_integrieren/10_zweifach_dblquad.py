#10_zweifach_dblquad.py
from math import *
from scipy.integrate import dblquad
#Funktionsdefinition
def f(x,y):
    return x+y**2
#obere Grenze, variabel
def y2(y):
    return 1-y/2
#Hauptprogramm
x1,x2=0,2 #konstant
y1=0      #y2 variabel
V= dblquad(f,x1,x2,y1,y2)[0]
print("Volumen V =",V)
