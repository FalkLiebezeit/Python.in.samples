#23_sympy_nichtlinear2.py
from sympy import symbols,nonlinsolve,N
x1,x2=symbols('x1,x2')
f1= x1**2+ x2   -5
f2=-x1   + x2**2-5
L=nonlinsolve([f1,f2],[x1,x2])
#print(L)
print(" x1 \t  x2")
print("(%3.3f | %3.3f)" %(N(L.args[0][0]),N(L.args[0][1])))
print("(%3.3f | %3.3f)" %(N(L.args[1][0]),N(L.args[1][1])))
print("(%3.3f | %3.3f)" %(N(L.args[2][0]),N(L.args[2][1])))
print("(%3.3f | %3.3f)" %(N(L.args[3][0]),N(L.args[3][1])))