#02_mul.py
from sympy import *
a,b,c=symbols("a b c")
T1=2*a+4*b-5*c
T2=4*a+2*b+3*c
T=T1*T2
print("Produkte der Terme")
pprint(T)
print("Terme ausmultipliziert")
print(expand(T))
print("Formatierte Ausgabe")
pprint(expand(T))


'''
from sympy import symbols, pprint,expand
print(type(T))
'''

