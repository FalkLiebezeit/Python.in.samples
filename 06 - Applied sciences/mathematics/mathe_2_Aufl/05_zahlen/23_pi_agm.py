#22_pi_agm.py
from mpmath import *
d = 61
mp.dps = d
eps = mpf(10**-d)
a,b,s,p = mpf(1),1/sqrt(mpf(2)),mpf(1/4),mpf(1)
while abs(a-b) > eps:
    an=(a+b)/2
    b=sqrt(a*b)
    c=an-a
    s=s-p*c**2
    p=2*p
    a=an
#Ausgabe
print(a**2/s)
print(pi)

# from sympy import pi,N
# print(N(pi,10000))
'''
#Quelle
David H. Bailey, Jonathan M. Borwein, Peter B. Borwein
and Simon Plouffe: The Quest for Pi
June 25, 1996, Seite 5
https://de.mathworks.com/company/newsletters/articles/computing-pi.html
'''
