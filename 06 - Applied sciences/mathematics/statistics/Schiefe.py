#L_09_05.py
import numpy as np
import statistics as st
import scipy.stats as sta

n=10000
sollwert=100
s=1

def schiefe(werte):
    n=len(werte)
    summe=0
    m=st.mean(werte)
    v=st.variance(werte)
    for i in range(n):
        summe=summe + np.power((werte[i]-m)/(v),3)
    return summe/n 

werte=sollwert + s*np.random.normal(size=n)

#Berechnungen
schiefe1=schiefe(werte)
schiefe2=sta.skew(werte)
if schiefe2<0:
    print("rechtssteil")
else:
    print("linkssteil")        
#Ausgabe
print("eigene Schiefe:",schiefe1)
print("SciPy- Schiefe:",schiefe2)





