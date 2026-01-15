#L_06_10.py
import numpy as np
N=500
eps=1e-6
def F(x):
    y=1-np.sin(x)**2 #a)
    #y=np.exp(-0.8*x) #b)
    #y=np.log(x)-x+2  #c)
    return y

x=np.empty(N+1)
x[0]=1 #Startwert 
for i in range(N):
    x[i+1]=F(x[i])
    dx=np.fabs(x[i+1]-x[i])
    if np.fabs(dx) < eps:break
    print("%3i | %3.6f | %3.6f | %3.6f"%(i,x[i],x[i+1],dx))

