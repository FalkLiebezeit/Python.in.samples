#08_konvergenz_pi.py
from math import *

def leibniz(eps,x1=3.1,x=3.2):
    summe=0
    k=1
    while abs(x-x1) > eps:
        x1=x
        summe=summe+(-1)**(k+1)/(2*k-1)
        k=k+1
        x=4*summe
    return round(x,15),k

def madhava(eps,x1=3.1,x=3.2):
    summe=0
    k=1
    while abs(x-x1) > eps:
        x1=x
        summe=summe + (-3)**(-k+1)/(2*k-1)
        k=k+1
        x=sqrt(12)*summe
    return round(x,15),k

def ramanujan(eps,x1=3.1,x=3.2):
    summe=k=0
    while abs(x-x1) > eps:
        x1=x
        zaehler=factorial(4*k)*(1103+26390*k)
        nenner= factorial(k)**4*396**(4*k)
        summe=summe + zaehler/nenner
        k=k+1
        x = 9801/(2*sqrt(2))*summe**-1
    return x,k
eps=1e-6 
#Ausgabe
print("\tπ\t\tn")
print(leibniz(eps),"\tLeibniz")
print(madhava(eps),"\t\tMadhava")
print(ramanujan(eps),"\t\tRamanujan")
print("",pi,"\t\tmath pi")
