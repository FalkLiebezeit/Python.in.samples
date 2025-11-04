#05_binom.py
from sympy import *
a,b=symbols("a b")
for n in range(7):
    p=(a+b)**n
    print(expand(p))



'''
pprint(expand(p))
print(type(p))
print(srepr(p))
'''