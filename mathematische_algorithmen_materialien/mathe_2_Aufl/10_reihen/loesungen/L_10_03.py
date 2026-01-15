#L_10_03.py
from sympy import *
n=symbols('n')

def a(n):
    #return n**2/E**n
    #return n**-n
    return (-1/(log(n+2)))**n
    
QK=limit(abs(a(n+1)/a(n)),n,oo)   #<1
WK=limit(Pow(abs(a(n)),1/n),n,oo) #<1
if (QK or WK) > 1:
    strKriterium="Die Reihe konvergiert nicht!"
elif (QK or WK) < 1 :
    strKriterium="Die Reihe konvergiert!"
elif (QK or WK) == 1 :
    strKriterium="Die Konvergenz ist unbestimmt!"
#Ausgabe
print("Quotientenkriterium:",QK)
print("Wurzelkriterium....:",WK)
print(strKriterium)




