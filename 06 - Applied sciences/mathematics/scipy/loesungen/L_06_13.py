#L_06_13.py
#gekoppeltes Fadenpendel
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
#Pendeldaten
g = 9.81    #Erdbeschleunigung
l= 0.2      #Pendellaengen
m= 0.2      #Pendelmassen
c=1         #Federkonstante
tmax=20
#DGL-System, der Unterstrich bedeutet 1. Ableitung nach der Zeit
def dgl(t,ya,l, m, c):
    phi1,w1,phi2,w2 = ya
    phi1_dt=w1
    w1_dt=-g/l*phi1-c/m*(phi1-phi2)
    phi2_dt=w2
    w2_dt=-g/l*phi2+c/m*(phi1-phi2)
    return [phi1_dt, w1_dt, phi2_dt, w2_dt]
#Anfangswerte
phi1 = 3
phi2 = 6
omega1 = omega2 = 0
ya =[np.radians(phi1),omega1,np.radians(phi2),omega2]
t = np.linspace(0,tmax,1000)
#Loesung des DGL-Systems
z=solve_ivp(dgl,[0,tmax],ya,args=(l,m,c),dense_output=True)
phi1,w1,phi2,w2 = z.sol(t)
auslenkung1,auslenkung2 = np.degrees(phi1),np.degrees(phi2)
#Objekte für zwei Unterdiagramme erzeugen
fig,ax=plt.subplots(2,1,figsize=(6,9))
#Auslenkung l1
ax[0].set_title("Pendel 1")
ax[0].plot(t,auslenkung1,"r",lw=2)
ax[0].set_ylabel(r"$\varphi_{1}$")
ax[0].grid(True)
#Auslenkung l2
ax[1].set_title("Pendel 2")
ax[1].plot(t,auslenkung2,'b',lw=2)
ax[1].set_xlabel("Zeit")
ax[1].set_ylabel(r"$\varphi_{2}$")
ax[1].grid(True)
fig.tight_layout()
plt.show()
'''
Quelle für DGL-System
Ahrens S. 1052
'''


