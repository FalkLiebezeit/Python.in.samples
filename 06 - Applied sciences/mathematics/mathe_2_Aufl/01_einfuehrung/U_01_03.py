#U_01_03.py
from math import exp
x=0
for i in range(5,16):
    x=10**-i
    y=(exp(x)-1)/x
    print(x,"",y)
    
#print(exp(1e-15))
