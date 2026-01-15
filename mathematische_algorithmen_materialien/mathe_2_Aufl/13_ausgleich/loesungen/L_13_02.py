#L_13_02.py
#Entladen eines Kondensators
import numpy as np
from numpy.linalg import solve
import matplotlib.pylab as plt
t=np.array([1,2,3,4,5])
u=np.array([6,3,1,0.5,0.1])
ln_u=np.log(u)
n=len(t)
A=np.array([[np.sum(t**2),np.sum(t)],
            [np.sum(t),n]])
b=np.array([np.sum(t*ln_u),np.sum(ln_u)])
L=solve(A,b)
A=L[0]
B=L[1]
U0=np.exp(B)
tau=A
print("Ladespannung : %2.3f V\nZeitkonstante: %2.3f s" %(U0, np.abs(tau)))
ta=np.linspace(0,np.max(t),500)
ua=U0*np.exp(tau*ta)
#Grafikbereich
fig,ax=plt.subplots()
ax.plot(t,u,'r+')
ax.plot(ta,ua,'b')
ax.set_title(r"$u_c=U_0e^{-\tau\cdot t}$")
ax.set_xlabel("t")
ax.set_ylabel(r"$u_c$")
plt.show()

