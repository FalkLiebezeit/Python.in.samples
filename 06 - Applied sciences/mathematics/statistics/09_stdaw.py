#09_stdaw.py
import numpy as np
import statistics as st
import time as t
n=100000
sollwert=100
s=2

def stdaw(werte):
    n=len(werte)
    summe=0
    for i in range(n):
        summe=summe+werte[i]
        mittelwert=summe/n
    sum_rq=0
    for i in range(n):
        sum_rq=sum_rq+(werte[i]-mittelwert)**2
    v=sum_rq/(n-1)
    return np.sqrt(v)

#werte=[1,2,3,4,5,6]
werte=sollwert + s*np.random.normal(size=n)
t1=t.time()
s1=stdaw(werte)
t2=t.time()
s2=st.stdev(werte)
t3=t.time()
s3=np.std(werte,ddof=1) 
t4=t.time()
print("\t\tStandardabweichung","Zeit",sep=("\t"))
print("eigene Version:",s1,t2-t1)
print("Python-Version:",s2,t3-t2)
print("NumPy-Version :",s3,t4-t3)



