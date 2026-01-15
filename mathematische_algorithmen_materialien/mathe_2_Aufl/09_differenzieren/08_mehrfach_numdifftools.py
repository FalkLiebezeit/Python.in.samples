#08_mehrfach_numdifftools.py
from numdifftools import Derivative
n=4 
#Funktionsdefinition
def f(x):
    return x**n/32
#Berechnung der Ableitungen
x0=2 #Stelle der Steigung
for i in range(1,n+1):
    y_ = Derivative(f,n=i)
    print(i,":",y_(x0))

'''
http://www.sciencedirect.com/science/article/pii/S1877750311001013
https://en.wikipedia.org/wiki/Automatic_differentiation
https://pythonhosted.org/algopy/index.html
https://numdifftools.readthedocs.io/en/latest/_modules/numdifftools/nd_algopy.html
'''
print(type(Derivative))