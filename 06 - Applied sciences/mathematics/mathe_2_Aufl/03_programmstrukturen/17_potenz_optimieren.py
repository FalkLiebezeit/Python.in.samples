#17_potenz.py
from math import log2
#einfache Lösung, Basis a, Exponent n
def pow1(a,n):
    p=a
    i=0 #zum zählen
    for _ in range(n-1):
        p=p*a 
        i=i+1 #proportional n
    return p,i
#optimierte Lösung
def pow2(a,n):
    p=1
    i=0 #zum zählen
    while n > 0:
        if n%2==1: #Exponent ungerade
            p=p*a
        a=a*a  #Basis quadrieren
        n=n//2 #Exponent halbieren
        i=i+1  #proportional log2(n)
    return p,i
#Hauptprogramm
a=2
n=1000  #n > 0
print("Exponent:",n)
print(pow1(a,n))
print(pow2(a,n))
print("log2(%d) = %3.3f" %(n,log2(n)))


