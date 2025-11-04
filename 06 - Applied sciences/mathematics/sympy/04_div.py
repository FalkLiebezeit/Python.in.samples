#04_div.py
from sympy import *
a,b,c=symbols("a b c")
T1=2*a+4*b-5*c
T2=4*a+2*b+3*c
T3=5*a-3*b+4*c
T=T1/(T2*T3)
print("Division der Terme")
pprint(T)
print("Terme ausmultipliziert")
print(expand(T))
print("Formatierte Ausgabe")
pprint(expand(T))

#print(type(T))
