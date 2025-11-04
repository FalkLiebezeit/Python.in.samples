#23_integral1.py
from sympy import *
x=symbols("x")
print("∫%sdx=%s" %(1/x,integrate(1/x)))
print("∫%sdx=%s" %(exp(-x),integrate(exp(-x))))
print("∫%sdx=%s" %(exp(-x)*x**2,integrate(exp(-x)*x**2)))
print("∫%sdx=%s" %(sin(x),integrate(sin(x))))
print("∫%sdx=%s" %(exp(-x)*sin(x),simplify(integrate(exp(-x)*sin(x)))))
#plot(exp(-x),integrate(exp(-x)),(x,0,10))
'''
#auch möglich, aber länger
#Funktionen
f1=1/x
f2=exp(-x)
f3=exp(-x)*x**2
f4=sin(x)
f5=exp(-x)*sin(x)
#unbestimmte Integrale
F1=integrate(f1)
F2=integrate(f2)
F3=integrate(f3)
F4=integrate(f4)
F5=integrate(f5)
print("∫%sdx=%s" %(f1,F1))
print("∫%sdx=%s" %(f2,F2))
print("∫%sdx=%s" %(f3,F3))
print("∫%sdx=%s" %(f4,F4))
print("∫%sdx=%s" %(f5,simplify(F5)))
'''


