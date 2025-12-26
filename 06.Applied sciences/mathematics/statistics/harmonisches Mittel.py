#L_09_01.py
import numpy as np
import scipy.stats as st
import time as t

n=100000
sollwert=100
s=1

def harmonisch(werte):
    n=len(werte)
    summe=0
    for i in range(n):
        summe=summe + 1.0/werte[i]
    mittelwert=1.0/summe
    return n*mittelwert   
    
#werte=[1,2,3,4,5]
werte=sollwert + s*np.random.normal(size=n)
#Berechnungen
t1=t.time()
h1=harmonisch(werte)
t2=t.time()
h2=st.hmean(werte)
t3=t.time()
#Ausgabe
print("\tharmonisches Mittel","Zeit",sep=2*("\t"))
print("meine Version:",h1,t2-t1)
print("SciPy Version:",h2,t3-t2)


