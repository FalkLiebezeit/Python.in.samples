#20_dgl_zweiter_ordnung.py
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
U0 = 100  #Eingangsspannung in V
R = 1.5   #Ankerwiderstand in Ohm
L = 0.025 #Ankerinduktivität in H
Mn=150    #Bemessungsmoment  in Nm
In=50     #Bemessungsstrom in A
J=0.2     #Trägheitsmoment in kgm^2
tmax=0.5  #Zeit in Sekunden
#DGL-System
def dgl(t,anfangswerte,R,L,C):
    uc,i = anfangswerte
    duc_dt = i/C
    di_dt = (U0 - R*C*duc_dt-uc)/L
    return [duc_dt, di_dt]

C = J*(In/Mn)**2 #dynamische Kapazität 
a0 = [0,0]       #Anfangswerte
ti=[0,tmax]      #Integrationsintervall
t = np.linspace(0,tmax,500)
z=solve_ivp(dgl,ti,a0,args=(R,L,C),dense_output=True)
uc,ic = z.sol(t)
fig,axes=plt.subplots(2,1,figsize=(6,6)) #Objekte erzeugen
#Kondensatorspannung
axes[0].plot(t, uc,"b",lw=2)
axes[0].set_title("Sprungantwort eines fremderregten Gleichstrommotors")
axes[0].set_ylabel('Ausgangsspannung in V')
#Stromverlauf
axes[1].plot(t, ic,"r",lw=2)
axes[1].set(xlabel='Zeit in Sekunden',ylabel='Ankerstrom in A')
axes[0].grid(True);axes[1].grid(True)
print("dynamische Kapazität:",C,"F")
fig.tight_layout()
fig.savefig('06_023.svg')
plt.show()

'''
fig.savefig('06_023.png')
fig.savefig('06_023.svg')
'''