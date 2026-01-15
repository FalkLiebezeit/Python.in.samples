#L_03_13.py
#pythagoräische Zahlentripel
from math import *
n=20
for a in range(1,n+1):
    for b in range(1,n+1):
        c2=a**2 + b**2
        c=int(sqrt(c2))
        if c2==c**2:
            print("(%3d, %3d, %3d)" %(a,b,c))
