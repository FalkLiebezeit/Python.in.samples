#12_scipy_dgl.py
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
#DGL-System
def dgl(t,xa,c,m,d):
    x,v = xa
    dx_dt = v
    dv_dt =  -c/m*x - d/m*v
    return dx_dt,dv_dt
#Daten
m=1.0  #Masse kg
d=0.2  #Dämpfung
c=9.87 #Federkonstante N/m
x0=5   #Anfangswert der Auslenkung
tmax=5
#Lösung der DGL
t = np.linspace(0,tmax,200)
z=solve_ivp(dgl,[0,tmax],[x0,0],args=(c,m,d),dense_output=True)
x,v=z.sol(t)
#Grafikbereich
fig,ax = plt.subplots(2,1,label='Feder-Masse-Schwinger')
#Auslenkung
ax[0].plot(t,x)
ax[0].set(ylabel='x',title='Auslenkung')
#Geschwindigkeit
ax[1].plot(t,v)
ax[1].set(xlabel='Zeit',ylabel='v',title='Geschwindigkeit')
fig.tight_layout()
plt.show()

# print(type(z.sol(t)))
'''
fig.savefig("/Users/veit/documents/Python_Mathe/Export_Mathe_Python_neu/Abbildungen/12_013.pdf")
fig.savefig("/Users/veit/documents/Python_Mathe/Export_Mathe_Python_neu/Abbildungen/12_013.svg")
'''