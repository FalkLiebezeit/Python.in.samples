#24_integral2.py
from sympy import *
x=symbols("x")
a,b=1,2 #Grenzen
F1=integrate(1/x,(x,a,b))
F2=integrate(exp(-x),(x,0,oo))
F3=integrate(exp(-x)*x**2,(x,0,oo))
F4=integrate(sin(x),(x,0,pi))
F5=integrate(exp(-x)*sin(x),(x,0,oo))
#Ausgabe
print("∫%s von %s bis %s = %s" %(1/x,a,b,F1))
print("∫%s von 0 bis ∞ = %s" %(exp(-x),F2))
print("∫%s von 0 bis ∞ = %s" %(exp(-x)*x**2,F3))
print("∫%s von 0 bis π = %s" %(sin(x),F4))
print("∫%s von 0 bis ∞ = %s" %(exp(-x)*sin(x),F5))
#plot(exp(-x)*sin(x),(x,0,10))
