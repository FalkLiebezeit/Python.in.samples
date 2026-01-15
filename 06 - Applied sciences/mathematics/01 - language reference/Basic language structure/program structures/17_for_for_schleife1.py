#17_for_for_schleife1.py
from math import *
k=8
for n in range(k):
    for k in range(n+1):
        print(comb(n,k),end=' ')
    print()
