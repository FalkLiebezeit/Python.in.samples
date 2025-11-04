#L_06_17.py
#SIRD-Modell aus der theoretischen Biologie
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
tmax=120
#Anfangswerte
S0=997  #nichtimmune Gesunde
I0=3    #Infizierte
R0=0    #Genesene
D0=0    #Todesfälle
N=S0+I0+R0 #Population
#Parameter
a=0.4   #Infektionsrate
g=0.035 #Genesungsrate
m=0.005 #Mortalitätsrate
#DGL-System
def dgl(t,ya):
    S,I,R,D=ya
    dS_dt=-a*S*I/N    #nichtimmune Gesunde
    dI_dt=a*S*I/N-g*I-m*I #Infizierte
    dR_dt=g*I         #Genesene
    dD_dt=m*I
    return [dS_dt,dI_dt,dR_dt,dD_dt]
#Anfangswerte
y0 = [S0,I0,R0,D0]
ti=[0,tmax]
t = np.linspace(0, tmax, 500)
z=solve_ivp(dgl,ti,y0,dense_output=True)
S,I,R,D = z.sol(t)
#zwei Objekte erzeugen
fig,ax = plt.subplots(figsize=(8,6))
ax.plot(t, S,'b',lw=2,label="Gesunde")
ax.plot(t, I,'r',lw=2,label="Infizierte")
ax.plot(t, R,'g',lw=2,label="Genesene")
ax.plot(t, D,'k',lw=2,label="Sterbefälle")
ax.legend(loc="best")
ax.set_xlabel("Zeit")
ax.set_ylabel("Individuen",color="red")
ax.grid(True)
plt.show()




