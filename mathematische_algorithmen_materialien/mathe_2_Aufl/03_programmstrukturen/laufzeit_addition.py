#laufzeit_addition.py
import time as t
N=1000
s=0
t1=t.time() #Sekunden
for n in range(0,N+1,1):
    s=s+n
t2=t.time() #Sekunden
delta_t=(t2-t1)*1e9 #ns
print(delta_t/N,"ns")

