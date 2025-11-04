#03_mul_linearfaktoren.py
from sympy import *
x=symbols("x")
lf=(x-1)*(x-2)*(x-3)*(x-4)
p=expand(lf)
print("\nDas Ausmultiplizieren der Linearfaktoren")
pprint(lf)
print("erzeugt das Polynom 4. Grades")
pprint(p)

'''
from sympy import pprint,symbols,expand
'''