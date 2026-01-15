#from math import sin
from numpy import sin
x=1.0
for i in range(1,10,1):
    h=10**-i
    y=sin(x+h)-sin(x)
    print("%1.2e %1.10e"%(h,y))
