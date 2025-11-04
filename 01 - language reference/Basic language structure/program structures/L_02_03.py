#L02_03.py
import math
def f(x):
    #return math.sin(x)
    return x**2

x=2
h=0.5
dy=(f(x+h)-f(x-h))/(2*h)
print(dy)    