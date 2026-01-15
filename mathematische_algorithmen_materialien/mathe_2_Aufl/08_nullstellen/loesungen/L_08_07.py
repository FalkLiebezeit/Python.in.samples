#L_08_07.py
#Fixpunkt als Funktion
from math import *
#Fixpunktgleichung
def F(x):
    y = cos(x)          #a)
    #y = sqrt(sin(x))    #b)
    #y = log(x**2/4+2)   #c)
    #y=sqrt(log(x+2)/2)  #d)
    return y
#Fixpunktverfahren
def fixpunkt(F,x,eps=1e-12):
    xa=0   #fuer Abbruch
    while abs(x-xa) > eps:
        xa=x 
        x=F(x)
    return x
#Hauptprogramm
x=0.2
print(fixpunkt(F,x))
