#L_03_fak_while.py
#Berechnung der Fakultaet mit for- und while-Schleife 
from math import *
#for-Schleife
def fak1(n):   
    f=1
    for i in range(n,1,-1):
        f = f*i
    return f
#while-Schleife
def fak2(n):   
    f=1
    while n > 1:
        f = f*n
        n=n-1
    return f
#Hauptprogramm
n=10
print(fak1(n))
print(fak2(n))
print(factorial(n))

'''
#Beispiel fuer 5!
5*4=20
20*3=60
60*2=120
120*1=120
'''