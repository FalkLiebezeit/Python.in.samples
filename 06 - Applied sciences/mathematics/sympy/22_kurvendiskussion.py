#22_kurvendiskussion.py
from sympy import *
x=symbols("x")

def f(x):
    #y=4*x**3-16*x
    #y=x**3-x**2-4*x+4
    y=-x**4+20*x**2-64
    return y
#Ableitungen
f_1=diff(f(x),x,1)
f_2=diff(f(x),x,2)
x0=solve(f(x),x) #Nullstellen
xe=solve(f_1,x)  #Extremstellen
xw=solve(f_2,x)  #Wendepunkt
#Ausgabe
print(f(x))  
print("Nullstellen:",x0)
print("Extremstellen:",xe)
print("Wendepunkte",xw)
#plot(f(x),(x,-5,5),xpos='right')