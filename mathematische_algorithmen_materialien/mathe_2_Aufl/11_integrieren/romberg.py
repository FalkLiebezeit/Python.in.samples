#Romberg-Verfahren
import numpy as np
#
def f(x):
    return x**2
#
def romberg(f,a,b,n=5):
    r = np.array([[0.0]*(n+1)]*(n+1))
    h = b - a
    r[0,0] = h*(f(a) + f(b))/2
    p2 = 1
    for i in range(1,n+1):
        h = h/2
        summe = 0
        p2 = 2*p2
        for k in range(1,p2,2):
            summe = summe + f(a + k*h)
        r[i,0] = r[i-1,0]/2 + summe*h
        p4 = 1
        for j in range(1,i+1):
            p4 = 4*p4
            r[i,j] = r[i,j-1] + (r[i,j-1] - r[i-1,j-1])/(p4 - 1)
    return r[-1,-1]
#
a,b=0,10
A=romberg(f,a,b,2)
print(A)

'''
#Quelle:
AUTHOR:
Jonathan R. Senning <jonathan.senning@gordon.edu>
Gordon College
February 17, 1999
Converted to Python August 2008
NOTES:
Based on an algorithm in "Numerical Mathematics and Computing"
4th Edition, by Cheney and Kincaid, Brooks-Cole, 1999.
'''
