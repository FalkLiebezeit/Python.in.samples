#15_forschleife2.py
import math
def f(x):
    #return x
    #return -x+1
    return math.exp(x)

a=0 #untere Grenze
b=1 #obere Grenze
n=1000
delta_x=(b-a)/n
r=0
x=a
for k in range(1,n+1):
    r=r+f(x)*delta_x
    x=a+k*delta_x
    #x=a-delta_x/2+k*delta_x
print("%6d %6.3f  %6.15f" %(k, x, r))    