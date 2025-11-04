#stdaw.py
import time as t
import numpy as np
import statistics as st
import scipy.stats as stats

n=100000
sollwert=100
s=1

def stdaw(werte):
    n=len(werte)
    summe=0
    sum_rq=0
    for i in range(n):
        summe=summe + werte[i]
        sum_rq=sum_rq + werte[i]**2    
    mittelwert=summe/n
    v=(sum_rq - n*mittelwert**2)/(n-1)
    return np.sqrt(v)   
    
#werte=[1,2,3,4,5]
werte=sollwert + s*np.random.normal(size=n)
t1=t.time()
s1=stdaw(werte)          #eigene
t2=t.time()
s2=st.stdev(werte)       #Python
t3=t.time()
s3=np.std(werte,ddof=1)  #NumpPy
t4=t.time()
s4=stats.tstd(werte)    #SciPy
t5=t.time()
#Ausgaben
print("\t\tStandardabweichung","Zeit",sep=("\t"))
print("eigene Version:",s1,t2-t1)
print("Python Version:",s2,t3-t2)
print("NumPy- Version:",s3,t4-t3)
print("SciPy- Version:",s4,t5-t4)



