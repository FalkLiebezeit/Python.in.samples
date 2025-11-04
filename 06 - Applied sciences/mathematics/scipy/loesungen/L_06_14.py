#L_06_14.py
#DGL-System mt zwei Differenzialgleichungen
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
xmax=10
a=1
b=1
c=1
d=0.1
#DGL-System
def dgl(x,ya):
    y1,y2=ya
    dy1_dx=a*y1-b*y1*y2
    dy2_dx=c*y1-d*y1*y2*x**2
    return [dy1_dx,dy2_dx]
#Anfangswerte
y0 = [1,1]
xi=[0,xmax]
x = np.linspace(0, xmax, 500)
z=solve_ivp(dgl,xi,y0,dense_output=True)
y1,y2= z.sol(x)
fig,ax=plt.subplots(3,1,figsize=(6,9))
#y1
ax[0].plot(x, y1,'r',lw=2)
ax[0].set_xlabel("x")
ax[0].set_ylabel("$y_1$")
ax[0].grid(True)
y2
ax[1].plot(x, y2,'b',lw=2)
ax[1].set_xlabel("x")
ax[1].set_ylabel("$y_2$")
ax[1].grid(True)
#Bahnkurve
ax[2].plot(y1, y2,'g',lw=2)
ax[2].set_xlabel("$y_1$")
ax[2].set_ylabel("$y_2$")
ax[2].grid(True)
fig.tight_layout()
plt.show()



