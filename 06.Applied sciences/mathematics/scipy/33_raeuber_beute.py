#35_raeuber_beute.py
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
K1=10e3 #Kapazitätsgrenze für Beutetiere
K2=1e3  #Kapazitätsgrenze für Raubtiere
beute=500
raeuber=50
r=0.25   #Reproduktionsrate Beute
b=0.001  #Beutewahrscheinlichkeit
s=0.5    #Sterberate Räuber
c,d = r/K1, s/K2
tmax=50  #Zeitraum
xy0=[beute,raeuber]
#DGL-System
def dgl(t,xy,r,b,s,c,d):
    N1,N2 = xy   #Anfangswerte
    dN1_dt= r*N1-b*N1*N2-c*N1**2 #Beute
    dN2_dt=-s*N2+b*N1*N2-d*N2**2 #Räuber
    return [dN1_dt,dN2_dt]
#Lösung der des DGL-Systems
t = np.linspace(0,tmax,500)
z=solve_ivp(dgl,[0,tmax],xy0,args=(r,b,s,c,d),dense_output=True)
N1, N2 = z.sol(t) #Trennung der Lösung
mbmean=int(np.mean(N1)) #Beute, Mittelwert
mrmean=int(np.mean(N2)) #Räuber, Mittelwert
fig,ax=plt.subplots(2,1,figsize=(6,6))
#Zeit-Diagramm
ax[0].plot(t, N1,"g--",lw=2,label="Beute")
ax[0].plot(t, N2,"r-",lw=2,label="Räuber")
ax[0].plot([0,tmax],[mbmean,mbmean],"g-.",lw=1)
ax[0].plot([0,tmax],[mrmean,mrmean],"r-.",lw=1)
ax[0].set(xlabel="Zeit",ylabel="$N_{1}, N_{2}$")
ax[0].legend(loc="best")
#Phasendiagramm
ax[1].plot(N1, N2,'b-',lw=1)
ax[1].set(xlabel="Beute",ylabel="Räuber",title="Phasendiagramm")
fig.tight_layout()
plt.show()
# fig.savefig('06_052.png')
# fig.savefig('06_052.svg')

