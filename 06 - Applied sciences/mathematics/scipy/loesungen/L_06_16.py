#L_06_16.py
"""
DGL 4. Ordnung
3y''''+2y''+y'+4y=cos(x)
Subtitutionen
y1=y,y2=y',y3=y'',y4=y'''
DGL-System 1. Ordnung
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
xmax=5

def dgl(x,ya):
    y1,y2,y3,y4=ya
    dy1_dx=y2
    dy2_dx=y3
    dy3_dx=y4
    dy4_dx=-4/3*y1-y2/3-2/3*y3+np.cos(x)
    return [dy1_dx,dy2_dx,dy3_dx,dy4_dx]
#Anfangswerte
y0 = [0,0,0,0]
xi=[0,xmax]
x = np.linspace(0, xmax, 500)
z=solve_ivp(dgl,xi,y0,dense_output=True)
y1,y2,y3,y4 = z.sol(x)
fig,ax=plt.subplots(4,1,figsize=(6,9))
#y1=y: Lösung der DGL !
ax[0].plot(x, y1,'r',lw=2)
ax[0].set_xlabel("x")
ax[0].set_ylabel("$y_1$")
ax[0].grid(True)
#y2
ax[1].plot(x, y2,'g',lw=2)
ax[1].set_xlabel("x")
ax[1].set_ylabel("$y_2$")
ax[1].grid(True)
#y3
ax[2].plot(x, y3,'b',lw=2)
ax[2].set_xlabel("x")
ax[2].set_ylabel("$y_3$")
ax[2].grid(True)
#y4 Lösung
ax[3].plot(x, y4,'y',lw=2)
ax[3].set_xlabel("x")
ax[3].set_ylabel("$y_3$")
ax[3].grid(True)
fig.tight_layout()
plt.show()





