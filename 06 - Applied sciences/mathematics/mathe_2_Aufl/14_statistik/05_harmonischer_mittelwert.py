#05_harmonischer_mittelwert.py
import numpy as np
from scipy.stats import hmean

def harmonischM(x):
    n=len(x)
    summe=0
    for i in range(n):
        summe=summe+1/x[i]
    return n/summe

a=np.loadtxt('daten.txt')
print("Harmonischer Mittelwert")
print(harmonischM(a))
print(hmean(a),"SciPy")