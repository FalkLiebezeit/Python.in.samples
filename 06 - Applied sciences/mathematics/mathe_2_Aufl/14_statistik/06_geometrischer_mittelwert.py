#06_geometrischer_mittelwert.py
import numpy  as np
from scipy.stats import gmean

def geometrischM(x):
    n=len(x)
    s=0
    for i in range(n):
        s=s+np.log(x[i])
    gm=s/n
    return np.exp(gm)

a=np.loadtxt('daten.txt')
print("Geometrischer Mittelwert")
print(geometrischM(a))
print(gmean(a),"SciPy")