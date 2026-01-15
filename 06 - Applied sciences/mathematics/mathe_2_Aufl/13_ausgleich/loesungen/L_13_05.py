#L_13_05.py
#Hyperbel:x**2/a**2-y**2/b**2=1
import numpy as np
from numpy.linalg import inv
import matplotlib.pylab as plt
x=np.array([1.7,2,3,4,5])
y=np.array([0,4.2,11.2,15,20.3])
n=len(x)
A=np.array([x**2,-y**2]).T
bs=np.ones(n)
L=inv(A.T@A)@A.T@bs
a,b=1./np.sqrt(L[0]),1./np.sqrt(L[1])
#a,b=1,4
print("Halbachsen der Hyperbel")
print("a =",a)
print("b =",b)
xa=np.linspace(a,5,100)
def ya(a,b,x):
    return b*np.sqrt(x**2/a**2-1)
#Grafikbereich
fig,ax=plt.subplots()
ax.plot(x,y,'ro',lw=2)
ax.plot(xa,ya(a,b,xa),'b--')
ax.set_title(r"$\frac{x^{2}}{a^{2}} -\frac{y^{2}}{b^{2}} =1$")
ax.set_xlabel("x")
ax.set_ylabel("y")
plt.show()




