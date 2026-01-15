#15_konvergenzradius.py
from sympy import *
n=symbols('n')

def a(n):
    return 1/factorial(n)           #e-Funktion
    #return (-1)**n/factorial(2*n+1) #Sinus
    #return (-1)**n/factorial(2*n)   #Kosinus
    #return 1/factorial(2*n+1) #Sinushyperbolikus
    #return 1/factorial(2*n)   #Cosinushyperbolikus
    #return (-1)**n/(2*n+1)    #Arkustangens |x|<1

R=limit(abs(a(n)/a(n+1)),n,oo)
print("Konvergenzradius:",R)

