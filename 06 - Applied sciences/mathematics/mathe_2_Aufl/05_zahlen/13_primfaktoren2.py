#16_primfaktoren2.py
from itertools import chain
from sympy import primefactors

def primfaktoren(n):
    f = [] 
    for i in chain([2], range(3, n//2+1, 2)):
        while n%i == 0:
            f.append(i)
            n = n//i
        if i > n: 
            break
    return f

z=1234566789
print("Primfaktoren von", z," sind:")
print(primfaktoren(z))
print(primefactors(z),"SymPy")

