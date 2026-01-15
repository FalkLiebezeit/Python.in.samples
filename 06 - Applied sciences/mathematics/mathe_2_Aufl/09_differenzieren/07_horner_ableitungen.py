#07_horner_ableitungen.py
from math import factorial
#Horner-Schema
def horner(a,x):
    n=len(a)-1
    p=[]
    for k in range(n+1):
        for j in range(n-1,k-1,-1):
            a[j] = a[j] + a[j+1]*x
        p.append(factorial(k)*a[k])
    return p
#Hauptprogramm
z=2
a=[2,1,2,3,4,5]
print(horner(a,z))

#a=[1,0,0,0,-2,3]
'''
b=list(reversed(a)) #vor Funktionsaufruf einfügen
import numpy as np
p=np.poly1d(b)
pdiff=np.polyder(p, m=1)
print(pdiff(z))
'''


