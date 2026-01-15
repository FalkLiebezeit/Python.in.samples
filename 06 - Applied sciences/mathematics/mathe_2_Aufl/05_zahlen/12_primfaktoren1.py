#15_primfaktoren1.py
from sympy import primefactors
def primfaktoren(n):
    f=[]
    t=2
    while t**2<=n:
        if n%t==0:
            f.append(t)
            n=n//t
        else:
            t=t+1
    f.append(n)
    return f

z=1234566789
print("Primfaktoren von",z," sind:")
print(primfaktoren(z))
print(primefactors(z),"SymPy")