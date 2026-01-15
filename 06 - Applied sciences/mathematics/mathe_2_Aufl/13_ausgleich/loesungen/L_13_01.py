#L_13_01.py
#v=v0*t-a*t
import numpy as np
from numpy.linalg import solve
import matplotlib.pylab as plt
t=np.array([1,2,3,4,5])
v=np.array([9,8,4,3,0.1])
n=len(t)
A=np.array([[np.sum(t**2),np.sum(t)],
            [np.sum(t),n]])
b=np.array([np.sum(t*v),np.sum(v)])
L=solve(A,b)
a,v0=L[0],L[1]
print("Beschleunigung a=%2.3f m/s^2\nAnfangsgeschwindigkeit v0=%2.3f m/s" %(a,v0))
ta=np.linspace(0,np.max(t),500)
va=a*ta+v0
#
fig,ax=plt.subplots()
ax.set_title(r"$v= v_0 - av$")
ax.plot(t,v,'r+')
ax.plot(ta,va,'b')
ax.set_ylim(0,15)
ax.set_xlabel("t")
ax.set_ylabel("v")
plt.show()
