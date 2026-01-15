#L03_18.py
#Laufzeitvergleich
import time as t
from math import *
#iterativ
def fak_i(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
#rekursiv
def fak_r(n):
    if (n==0):
        return 1
    else:
        return n*fak_r(n-1)
#Hauptprogramm    
N = 60
#rekursiv
t1=t.time()
f1=fak_r(N)
t2=t.time()
delta_t1=(t2-t1)*1e3 #ms
#iterativ
t3=t.time()
f2=fak_i(N)
t4=t.time()
delta_t2=(t4-t3)*1e3 #ms
#factorial
t5=t.time()
f3=factorial(N)
t6=t.time()
delta_t3=(t6-t5)*1e3 #ms
print(N,"! =",f1,"",delta_t1)
print(N,"! =",f2,"",delta_t2)
print(N,"! =",f3,"",delta_t3)
print(delta_t1/delta_t2)

'''
from math import *
print(N,"! =",factorial(N))
'''


