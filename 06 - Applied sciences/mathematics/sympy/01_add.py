#01_add.py
from sympy import *
a,b,c,d=symbols("a b c d")
T1=9*a+7*b-2*c+3*d
T2=8*a+2*b+3*c+4*d
T3=7*a-3*b+2*c+5*d
T4=4*a+2*b+5*c-6*d
T=T1+T2+T3+T4
print("Summe der Terme")
pprint(T)


'''
from sympy import symbols, pprint
print(type(a))
print(type(T))
print(srepr(T))
'''

