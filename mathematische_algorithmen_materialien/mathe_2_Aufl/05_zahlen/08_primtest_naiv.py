#11_primtest_naiv.py
from math import sqrt,ceil
def istPrim(zahl):
    kmax=ceil(sqrt(zahl))
    for k in range(2,kmax):
        if zahl%k==0:          #ohne Rest teilbar
            return zahl, False #also keine Primzahl
    return zahl, True #ist eine Primzahl
#Hauptprogramm
for z in [11,191,499,9091,333667,2**11-1]:
    print(istPrim(z))

