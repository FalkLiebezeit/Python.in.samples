#10_woelbung.py
import numpy as np
from scipy.stats import kurtosis,norm,laplace,uniform
a1 = uniform.rvs(size=1000, random_state=3)#Gleichverteilung
a2 = laplace.rvs(size=1000, random_state=3)#Laplace
a3 = norm.rvs(size=1000, random_state=3) #Normalverteilung

def woelbung(x):
    n=len(x)
    summe=0
    for i in range(n):
        summe=summe+x[i]
    m=summe/n         #Mittelwert
    v=0
    for i in range(n):
        v=v+(x[i]-m)**2
    s=np.sqrt(v/(n-1)) #Standardabweichung
    w=0
    for i in range(n):
        w=w+((x[i]-m)/s)**4
    return w/n-3

print("Wölbung")
print("Gleichverteilung")
print(woelbung(a1))
print(kurtosis(a1),"SciPy")
print("Laplace-Verteilung")
print(woelbung(a2))
print(kurtosis(a2),"SciPy")
print("Normalverteilung")
print(woelbung(a3))
print(kurtosis(a3),"SciPy")





