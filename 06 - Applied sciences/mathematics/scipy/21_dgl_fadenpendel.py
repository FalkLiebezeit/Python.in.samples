#21_dgl_fadenpendel.py
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
l=10       #Länge des Pendels in m
d=1    #Durchmesser der Kugel in dm
phi0=179   #Auslenkung
cw=0.3      #Widerstandsbeiwert für Kugel
rho_K=7.85  #Dichte von Stahl kg/dm^2
rho_L=1.28  #Dichte von Luft kg/m^3
g=9.81      #Erdbeschleunigung
tmax=50
#DGL-System
def dgl(t,ya,b,w02):
    phi, w = ya
    dphi_dt = w
    dw_dt = -b*np.abs(w)*w-w02*np.sin(phi)
    return [dphi_dt,dw_dt]
#Berechnungen
r=d/2       #Radius der Kugel in dm
A=np.pi*(0.1*r)**2 #Kreisfläche in m^2
m=rho_K*(4/3)*np.pi*r**3   #Masse der Kugel in kg
b=cw*rho_L*A*l/(2*m) #Dämpfungskonstante
w02=g/l
T=2.0*np.pi*np.sqrt(l/g)
f=1.0/T    #Frequenz
vmax=np.sqrt(2*g*l*(1-np.cos(np.radians(phi0))))
#Lösung der DGL
y0 = [np.radians(phi0),0]
t = np.linspace(0, tmax, 500)
z=solve_ivp(dgl,[0,tmax],y0,args=(b,w02),dense_output=True)
phi, w = z.sol(t) 
v=l*w
#Ausgabe
fig,ax=plt.subplots(2,1,figsize=(6,6))
#Auslenkung
ax[0].plot(t, np.degrees(phi),'r-',lw=2)
ax[0].set(ylabel=r"$\varphi$ in °",title="Fadenpendel")
#Geschwindigkeit
ax[1].plot(t, v,'b-',lw=2)
ax[1].set(xlabel='Zeit in s',ylabel="v in m/s")
[ax[i].grid(True) for i in range(len(ax))]
fig.tight_layout()
print("Masse der Kugel %3.2f kg"%m)
print("Periodendauer %3.2f s"%T)
print("Frequenz %3.2f Hz"%f)
print("Dämpfung %3.4f"%b)
print("maximale Geschwindigkeit %3.2f m/s"%vmax)
plt.show()

# fig.savefig('06_026.png')
# fig.savefig('06_026.svg')
'''
#Foucaultsches Pendel 
d=1.896
l=67
phi=1.71 
'''


