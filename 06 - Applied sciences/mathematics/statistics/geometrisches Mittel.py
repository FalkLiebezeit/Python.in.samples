#L_09_02.py
import time as t
import numpy as np
import scipy.stats as st

n=100
sollwert=100
s=1

def geometrisch(werte):
    n=len(werte)
    p=werte[0]
    for i in range(1,n):
        p=p*werte[i]
    p=np.power(p,1/n)
    return p  
    
#werte=[1,2,3,4,5]
werte=sollwert + s*np.random.normal(size=n)
#Berechnungen
t1=t.time()
g1=geometrisch(werte)
t2=t.time()
g2=st.gmean(werte)
t3=t.time()
#Ausgabe
print("\tgeometrisches Mittel","Zeit",sep=2*("\t"))
print("meine Version:",g1,t2-t1)
print("SciPy Version:",g2,t3-t2)



