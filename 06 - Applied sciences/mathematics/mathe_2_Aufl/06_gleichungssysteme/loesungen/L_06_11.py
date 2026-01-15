#L_06_11.py
from math import *
eps=1e-6
def F(x):
    return x**5 + 0.5
x=-1     #Startwert
#x=0
#x=0.8   #Instabil 
xa=0.1   #Abbruch
while fabs(x-xa)>eps:
    xa=x 
    x=F(x)
    print(x)
