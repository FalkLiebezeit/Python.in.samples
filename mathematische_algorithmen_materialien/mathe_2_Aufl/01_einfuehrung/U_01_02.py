#U_01_02.py
a=4.2348
b=3.2349
c=2.1234
x=a*c-b*c
y=(a-b)*c
print(x)
print(y)
#genauer
from decimal import *
getcontext().prec = 16
a,b,c=Decimal(a),Decimal(b),Decimal(c)
u=a*c-b*c
v=(a-b)*c
print(u)
print(v)
'''
from mpmath import *
a=mpf(a)
b=mpf(b)
c=mpf(c)
u=a*c-b*c
v=(a-b)*c
print(u)
print(v)
'''