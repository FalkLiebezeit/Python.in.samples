#06_12b.py
from sympy import *
x1,x2,x3=symbols('x1,x2,x3',real=True)
f1=x1*x2 +x2 +x3 -13
f2=2*x1 + x1*x2  +x3 -14
f3=x1 + x2 +x2*x3 - 17
L=nonlinsolve([f1,f2,f3],[x1,x2,x3])
print(L)
print(" x1 \t  x2 \t  x3")
print("(%3.3f | %3.3f | %3.3f)" %(N(L.args[0][0]),N(L.args[0][1]),N(L.args[0][2])))
print("(%3.3f | %3.3f | %3.3f)" %(N(L.args[1][0]),N(L.args[1][1]),N(L.args[1][2])))
print("(%3.3f | %3.3f | %3.3f)" %(N(L.args[2][0]),N(L.args[2][1]),N(L.args[2][2])))
