#laufzeit_multiplikation.py
import time as t
n=1000
f=1
t1=t.time() #Sekunden
for i in range(1,n+1,1):
    f=f*i
t2=t.time() #Sekunden
delta_t=(t2-t1)*1e9 #ns
print(delta_t/n,"ns")
