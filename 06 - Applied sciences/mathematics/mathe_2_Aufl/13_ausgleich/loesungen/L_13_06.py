#L_13_06.py
import numpy as np
from numpy.linalg import solve
import matplotlib.pylab as plt
#
xi=np.array([1,2,3,4,5])
yi=np.array([502,995,2011,3874,8021])
ln_y=np.log(yi)
n=len(xi)
A=np.array([[np.sum(xi**2),np.sum(xi)],
            [np.sum(xi),n]])
y=np.array([np.sum(xi*ln_y),np.sum(ln_y)])
L=solve(A,y)
A,B=L[0],L[1]
a=np.exp(B)
b=A
print("a=%2.3f b=%2.3f" %(a,b))
xa=np.linspace(0,np.max(xi),500)
ya=a*np.exp(b*xa)
#Grafikbereich
fig,ax=plt.subplots()
ax.plot(xi,yi,'r+')
ax.plot(xa,ya,'b')
ax.set_title(r"$n=ae^{bt}$")
ax.set_xlabel("t in Tagen")
ax.set_ylabel("Anzahl n")
plt.show()

