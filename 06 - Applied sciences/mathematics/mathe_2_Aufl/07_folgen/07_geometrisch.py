#07_geometrisch.py
from math import sqrt
def a(a1,q,n):
    return a1*q**(n-1)
#Hauptprogramm    
a1=5
q=3
print("n a1*q^(n-1)    q^n/q^(n-1)  √(q(n-1)*q(n+1))")
for n in range(1,6):
    f1=a(a1,q,n)
    f2=a(a1,q,n-1)
    f3=sqrt(a(a1,q,n-1)*a(a1,q,n+1))
    print("%i %5.0f \t%3.0f \t\t %3.0f"%(n,f1,f1/f2,f3))



