#13_vereinfachen.py
from sympy import *
a,b,c,n,x,y=symbols("a b c n x y")
#Terme
t1=exp(log(x)+log(y))
t2=n*x**n/x
t3=a**3/((a-b)*(a-c))+b**3/((b-c)*(b-a))+c**3/((c-a)*(c-b))
t4=2*sqrt(1/x)-1/sqrt(x)
t5=(y**2 + y)/(y*sin(a)**2 + y*cos(a)**2)
#Ausgaben
print("1: exp(log(x)+log(y)), vereinfacht:",t1)
print("2:",t2,",vereinfacht:",simplify(t2))
print("3:",t3,"\n   vereinfacht:",simplify(t3))
print("4:",t4,",vereinfacht",simplify(t4))
print("5:",t5,",vereinfacht:",simplify(t5))

'''
from sympy.abc import a,b,c,n,x,y
from sympy import pprint,symbols,simplify,cos,sin,exp,log,sqrt
'''