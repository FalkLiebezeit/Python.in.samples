#16_fakultaet_rekursiv.py
def fakultaet(n):
    if n == 0:
        return 1
    else:
        return n*fakultaet(n-1)
#Funktionsaufrufe

print(fakultaet(5))
#print(fakultaet(6))
#print(fakultaet(32))

'''
#zum testen
fakultaet(49)/(fakultaet(43)*fakultaet(6))
from timeit import *
timeit(str(fakultaet(800)))
'''