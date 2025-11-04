#36_epidemie.py
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
tmax=120
S0=997  #nicht immune Gesunde
I0=3    #Infizierte
R0=0    #Genesene
N=S0+I0+R0 #Population
b=0.4  #Infektionsrate
g=0.04 #Genesungsrate
#DGL-System
def dgl(t,ya):
    S,I,R=ya
    dS_dt=-b*S*I/N    #nicht immune Gesunde
    dI_dt=b*S*I/N-g*I #Infizierte
    dR_dt=g*I         #Genesene, Recover
    return [dS_dt,dI_dt,dR_dt]
#Anfangswerte
y0 = [S0,I0,R0]
t = np.linspace(0, tmax, 500)
z=solve_ivp(dgl,[0,tmax],y0,dense_output=True)
S, I, R = z.sol(t)
fig, ax = plt.subplots()
ax.plot(t, S,'b-',label="Gesunde")
ax.plot(t, I,'r--',label="Infizierte")
ax.plot(t, R,'g-.',label="Genesene")
ax.legend(loc='best')
ax.set(xlabel="Zeit",ylabel="Individuen")
ax.grid(True)
plt.show()








