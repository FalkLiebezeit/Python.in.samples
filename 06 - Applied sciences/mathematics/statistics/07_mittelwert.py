#07_mittelwert.py
import numpy as np
import statistics as st
import time as t
n=100000
sollwert=50
s=1

def mittelwert(werte):
    n=len(werte)
    summe=0
    for i in range(n):
        summe=summe+werte[i]   
    return summe/n
    
#werte=[1,2,3,4,5,6]
werte=sollwert + s*np.random.normal(size=n)
t1=t.time()
m1=mittelwert(werte)
t2=t.time()
m2=st.mean(werte)
t3=t.time()
m3=np.mean(werte)
t4=t.time()
print("\tarithmetischer Mittelwert","Zeit",sep=4*("\t"))
print("eigene Version:",m1,t2-t1,sep=2*("\t"))
print("Python-Version:",m2,t3-t2,sep=2*("\t"))
print("NumPy-Version :",m3,t4-t3,sep=2*("\t"))



