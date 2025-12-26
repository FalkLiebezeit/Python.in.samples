#21_differential.py
from sympy import *
x,a,b,A=symbols("x a b A")
y1=x**4-3*x**3+x**2-20  #Potenzregel
y2=sin(x)*cos(x)        #Produktregel
y3=(x**3-4*x+3)/(x+4)   #Quotientenregel
y4=A*exp(-a*x)*sin(b*x) #Kettenregel
#Berechnungen und Ausgaben
print("1. Ableitung von:",y1,"\n", diff(y1,x))
print("1. Ableitung von:",y2,"\n", diff(y2,x))
print("1. Ableitung von:",y3,"\n", diff(y3,x))
print("1. Ableitung von:",y4,"\n", diff(y4,x,1))
print("2. Ableitung von:",y4,"\n", diff(y4,x,2))
print("3. Ableitung von:",y4,"\n", diff(y4,x,3))



       