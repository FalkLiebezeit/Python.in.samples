#14_reihenentwicklung.py
from sympy import *
x=symbols('x')
n=10
a=cos(x).series(x,0,n)
b=(sin(x)*I).series(x,0,n)
c=exp(x*I).series(x,0,n)
d=a+b
#Ausgabe
print("Reihenentwicklung cos\n",a)
print("\nReihenentwicklung sin\n",b)
print("\nReihenentwicklung cos+sin\n",c)
print("\nReihenentwicklung e-Funktion\n",d)



