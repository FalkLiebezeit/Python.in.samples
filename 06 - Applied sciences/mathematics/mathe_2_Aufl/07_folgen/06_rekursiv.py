#06_rekursiv.py
a=1 #Startwert
for n in range(1,10):
    a = a/2 + 1
    print(n," ",a)
'''
from fractions import Fraction
a=Fraction(1/1)
for n in range(1,10):
    a = a/2 + 1
    print(n," ",a)
'''

