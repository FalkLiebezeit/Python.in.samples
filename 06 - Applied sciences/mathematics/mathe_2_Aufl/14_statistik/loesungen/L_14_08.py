#L_14_08.py
import numpy as np
from scipy.stats import skew

n=1000
sollwert=100
s=1

def schiefe(x):
    n=len(x)
    summe=0
    m=np.mean(x)
    s=np.std(x)
    for i in range(n):
        summe=summe + ((x[i]-m)/s)**3
    return summe/n 

a=np.random.normal(sollwert,s,size=n)
#Berechnungen
schiefe1=schiefe(a)
schiefe2=skew(a)
if schiefe2<0:
    print("rechtssteile ",end='')
else:
    print("linkssteile ",end='')        
#Ausgabe
print("Schiefe")
print(schiefe1)
print(schiefe2,"SciPy")






