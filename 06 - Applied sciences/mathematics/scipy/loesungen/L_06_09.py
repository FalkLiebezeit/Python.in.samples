#L_06_09.py
#Stabpendel
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
l=1    #Länge des Pendels in m
d=0.5  #Dämpfung
g=9.81
phi0=60
tmax=10
#DGL-System
def dgl(t,ya,l,d):
    phi, w = ya
    dphi_dt = w
    dw_dt =-3*g/(2*l)*np.sin(phi)-d*w
    return [dphi_dt,dw_dt]
#Anfangswerte
y0 = [np.radians(phi0),0]
ti=[0.1,tmax]
t = np.linspace(0, tmax, 500)
z=solve_ivp(dgl,ti,y0,args=(l,d),dense_output=True)
phi,w = z.sol(t)
x=np.sin(phi)
y=l-np.cos(phi)
phi = np.degrees(phi)
fig,ax=plt.subplots(3,1,figsize=(6,9))
#Auslenkung
ax[0].set_title("Auslenkung")
ax[0].plot(t, phi,'r',lw=2)
ax[0].set_title("Auslenkung")
ax[0].set_xlabel("Zeit")
ax[0].set_ylabel(r"$\varphi$ in °")
ax[0].grid(True)
#Winkelgeschwindigkeit
ax[1].set_title("Winkelgeschwindigkeit")
ax[1].plot(t, w,'b',lw=2)
ax[1].set_xlabel("Zeit")
ax[1].set_ylabel("$\omega$ in 1/s")
ax[1].grid(True)
#Bahnkurve (Trajektorie)
ax[2].set_title("Bahnkurve")
ax[2].plot(x, y,'g',lw=2)
ax[2].set_xlabel("x")
ax[2].set_ylabel("y")
ax[2].grid(True)
fig.tight_layout()
plt.show()


