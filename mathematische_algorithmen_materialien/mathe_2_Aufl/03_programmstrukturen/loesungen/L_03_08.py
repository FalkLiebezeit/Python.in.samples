#L03_08.py
from math import sqrt
def dreieck(a,b):
    '''Berechnet die Hypotenuse c, die Abschnitte q, p
       und die Höhe h eines rechtwinkligen Dreiecks.
       Parameter: Kathete a und b.'''
    c=sqrt(a**2 + b**2)
    p=a**2/c
    q=b**2/c
    h=sqrt(q*p)
    return c,q,p,h

a1=3
b1=4
c,q,p,h=dreieck(a1,b1)
print("c =",c)
print("q =",q)
print("p =",p)
print("h =",h)
