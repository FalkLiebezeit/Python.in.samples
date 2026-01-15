#l_03_09.py
#Berechnet Umfang, Fläche und Winkel eines Dreiecks
from math import *
def dreieck(a,b,c):
    U=a+b+c
    s=U/2
    A=sqrt(s*((s-a)*(s-b)*(s-c)))
    alpha=degrees(acos((b**2+c**2-a**2)/(2*b*c)))
    beta= degrees(acos((a**2+c**2-b**2)/(2*a*c)))
    gamma=degrees(acos((a**2+b**2-c**2)/(2*a*b)))
    return U,A,alpha,beta,gamma

a1=7
b1=4
c1=5

U,A,alpha,beta,gamma=dreieck(a1,b1,c1)
print("Umfang:",U)
print("Fläche:",A)
print("alpha :",alpha)
print("beta  :",beta)
print("gamma :",gamma)
print("Winkelsumme:",alpha+beta+gamma)