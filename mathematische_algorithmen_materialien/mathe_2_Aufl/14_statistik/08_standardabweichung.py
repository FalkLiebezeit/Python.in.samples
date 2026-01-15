#08_standardabweichung.py
import numpy as np

def standardabweichung(x):
    n=len(x)
    summe=0
    for i in range(n):
        summe=summe+x[i]
    m=summe/n
    v=0
    for i in range(n):
        v=v+(x[i]-m)**2
    return np.sqrt(v/(n-1))

a=np.loadtxt('c:/Users/Falk/source/repos/Python.in.samples/12 - DataInput/daten.txt')
print("Standardabweichung")
print(standardabweichung(a))
print(np.std(a,ddof=1),"NumPy")