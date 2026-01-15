#10_sympy_konvergenzkriterien.py
from sympy import *
n=symbols('n')

def a(n):
    return 1/n                 #harmonische Folge
    #return 1/factorial(n-1)     #Eulersche Zahl e
    #return 4*(-1)**(n+1)/(2*n-1)#Kreiszahl π
    #return n**2/2**n           #Grenzwert 6

QK=limit(abs(a(n+1)/a(n)),n,oo)   #<1
WK=limit(Pow(abs(a(n)),1/n),n,oo) #<1
g=limit(a(n),n,oo)
#Ausgabe
print("Quotientenkriterium:",QK)
print("Wurzelkriterium....:",WK)
print("Grenzwert.......:",g)



