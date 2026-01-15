#L_12_05.py
from sympy import *
x = symbols('x')
y = Function('y')
dgl1=diff(y(x),x) -   2*y(x) - 1 
dgl2=diff(y(x),x,2) - 4*diff(y(x),x) + 3*y(x) - 5*exp(3*x)
dgl3=diff(y(x),x,3) - 2*diff(y(x),x,2)  - 8*diff(y(x),x)
dgl4=diff(y(x),x,4) + 2*diff(y(x),x,2) + y(x)
print("a) ",dsolve(dgl1))
print("b) ",dsolve(dgl2))
print("c) ",dsolve(dgl3))
print("d) ",dsolve(dgl4))