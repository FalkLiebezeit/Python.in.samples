#L_02_06.py
'''bestimmtes Integral'''
import math
def f(x):
    #return x
    #return -x+1
    return math.exp(x)

a=0 #untere Grenze
b=1 #obere Grenze
n=1000
h=(b-a)/n
r=0
for k in range(1,n+1):
    r=r+f(a-h/2+k*h)*h
print("%6d  %6.15f" %(k, r))    
