#L_05_05.py
from sympy import *
x=symbols("x")
y=Function("f")(x)
#DGL 1. Ordnung
dgl1=2*Derivative(y,x)+8*y #a
dgl2=Derivative(y,x)/5-6*y #b
dgl3=3*Derivative(y,x)-6*y #c
#DGL 2. Ordnung
dgl4=7*Derivative(y,x,x)-4*Derivative(y,x)-3*y-6 #d
dgl5=Derivative(y,x,x)-10*Derivative(y,x)+9*y-9*x #e
#Lösungen
print(dsolve(dgl1,y))  
print(dsolve(dgl2,y)) 
print(dsolve(dgl3,y))
print(dsolve(dgl4,y))
print(dsolve(dgl5,y))


