#11_solve3.py
from sympy import *
a,b,x=symbols("a,b,x")
#Gleichungen
y1=x**4-7*x**3-13*x**2+79*x+84
y2=log(sqrt(x)-2)-1
y3=exp(sqrt(x)-2)-1
y4=sinh(x)-10
y5=cosh(x)-10
#Ausgaben
print("Lösungen")
print("f(x)=%s|f(x=0)=%s" %(y1,solve(y1,x)))
print("f(x)=%s|f(x=0)=%s" %(y2,solve(y2,x)))
print("f(x)=%s|f(x=0)=%s" %(y3,solve(y3,x)))
print("f(x)=%s|f(x=0)=%s" %(y4,solve(y4,x)))
print("f(x)=%s|f(x=0)=%s" %(y5,solve(y5,x)))

'''
plot(y1,(x,-5,8))
plot(y2,(x,0,5))
plot(y3,(x,0,5))
plot(y4,(x,0,5))
plot(y5,(x,-5,5))
'''