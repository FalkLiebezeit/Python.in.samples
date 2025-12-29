#L_06_11.py
#Federpendel mit Phasendiagramm
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
m=0.5   #Masse 
d=0.2   #Dämpfung
c= 5    #Federkonstane N/m
ya=0.1    #Auslenkung in m
#DGL
def dgl(t,y0,D,w02):
    y,v=y0
    dy_dt=v
    dv_dt=-D*v-w02*y
    return [dy_dt,dv_dt]
#Berechnungen
w02=c/m
D=d/m
#Lösung der DGL
y0=[ya,0] #Anfangswert
t=np.linspace(0,10,500)
z=solve_ivp(dgl,[0,10],y0,args=(D,w02),dense_output=True)
y,v=z.sol(t)
#Grafikbereich
fig, ax=plt.subplots(3,figsize=(6,9))
#Auslenkung
ax[0].plot(t,y)
ax[0].set(xlabel='t',ylabel='y',title='Auslenkung')
#Geschwindigkeit
ax[1].plot(t,v)
ax[1].set(xlabel='t',ylabel='v',title='Geschwindigkeit')
#Phasendiagramm
ax[2].plot(y,v)
ax[2].set(xlabel='y',ylabel='v',title='Phasendiagramm')
fig.tight_layout()
plt.show()
