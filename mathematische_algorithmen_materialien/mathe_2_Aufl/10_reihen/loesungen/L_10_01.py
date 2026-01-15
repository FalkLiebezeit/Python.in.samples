#L_10_01.py
from math import *
import matplotlib.pyplot as plt
n=20
def a(n):
    return 4*(-1)**n/(2*n+1)

summe=0
for k in range(0,n+1):
    summe=summe + a(k)
    plt.scatter(k,summe,marker='x',color='r')
plt.hlines(pi,0,20)
plt.xlabel('k')
plt.ylabel('Summe')
plt.show()

