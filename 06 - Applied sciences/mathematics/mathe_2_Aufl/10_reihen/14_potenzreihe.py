#14_potenzreihe.py
from math import *
x=2   #Entwicklungspunkt
m=20  #Anzahl der Summanden

def a(n):
    return 1/factorial(n) #e-Funktion

summe=0
for n in range(m):
    summe=summe + a(n)*x**n
print(summe)
print(exp(x),"genau")

    