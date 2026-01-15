#L_05_03.py
#Linearkombination
from sympy import gcdex
a=12
b=34
c=gcdex(a,b)
print("ggT(a,b)=u*a + v*b")
print("a =",a,", b =",b)
print("Der größete gemeinsame Teiler ist:",c[2])
print(c)
print("u =",c[0],", v =",c[1])
print(c[0]*a,"+",c[1]*b,"=",c[2])