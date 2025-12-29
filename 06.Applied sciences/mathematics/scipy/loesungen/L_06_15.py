#L_06_15.py
#DGL-System mit drei Differenzialgleichungen
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
xmax=1
#DGL-System
def dgl(x,ya):
    y1,y2,y3=ya
    dy1_dx=y2+2*y3
    dy2_dx=-x*y1+y2
    dy3_dx=y1+y2
    return [dy1_dx,dy2_dx,dy3_dx]
#Anfangswerte
y0 = [1,0,1]
xi=[0,xmax]
x = np.linspace(0, xmax, 500)
z=solve_ivp(dgl,xi,y0,dense_output=True)
y1,y2,y3= z.sol(x)
fig,axes=plt.subplots(3,1,figsize=(6,9))
#y1
axes[0].plot(x, y1,'r',lw=2)
axes[0].set_xlabel("x")
axes[0].set_ylabel("$y_1$")
axes[0].grid(True)
#y2
axes[1].plot(x, y2,'g',lw=2)
axes[1].set_xlabel("x")
axes[1].set_ylabel("$y_2$")
axes[1].grid(True)
#y3
axes[2].plot(x, y3,'b',lw=2)
axes[2].set_xlabel("x")
axes[2].set_ylabel("$y_3$")
axes[2].grid(True)
fig.tight_layout()
plt.show()




