#06_konvergenz_e.py
from math import *
n=10
summe=0
for k in range(n+1):
    summe=summe + 1/factorial(k)
    print(k,"\t",summe)
print("genau:\t",exp(1))