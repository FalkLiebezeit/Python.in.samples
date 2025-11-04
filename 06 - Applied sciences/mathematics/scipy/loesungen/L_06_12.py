##L_06_12.py
#Simulation des Foucaultschen Pendels 
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
l=67           #Länge des Pendels in m
d=1.896        #Durchmesser der Kugel in dm
auslenkung=2   #Auslenkung in m
cw=0.3         #Widerstandsbeiwert für Kugel
rho_K=7.85     #Dichte von Stahl kg/dm^2
rho_L=1.28     #Dichte von Luft kg/m^3
g=9.81         #Erdbeschleunigung
tmax=50
#DGL-System
def dgl(t,ya,b,w02):
    phi, w = ya
    dphi_dt = w
    dw_dt = -b*np.abs(w)*w-w02*np.sin(phi)
    return [dphi_dt,dw_dt]
#Berechnungen
phi0=np.arcsin(auslenkung/l) #Auslenkwinkel
r=d/2              #Radius der Kugel in dm
A=np.pi*(0.1*r)**2 #Kreisfläche in m^2
m=rho_K*(4/3)*np.pi*r**3   #Masse der Kugel in kg
b=cw*rho_L*A*l/(2*m)       #Dämpfungskonstante
w02=g/l
T=2.0*np.pi*np.sqrt(l/g)
f=1.0/T    #Frequenz
vmax=np.sqrt(2*g*l*(1-np.cos(phi0)))
#Lösung der DGL
y0 = [phi0,0]
t = np.linspace(0, tmax, 500)
z=solve_ivp(dgl,[0,tmax],y0,args=(b,w02),dense_output=True)
phi, w = z.sol(t) 
x= l*np.sin(phi)
y=l-l*np.cos(phi)
v=l*w
#Ausgabe
fig,ax=plt.subplots(2,2,figsize=(12,8))
#Auslenkung
ax[0,0].plot(t, x,'r-',lw=2)
ax[0,0].set(ylabel="Auslenkung in m",title="Auslenkung")
#Geschwindigkeit
ax[1,0].plot(t, v,'b-',lw=2)
ax[1,0].set(xlabel='Zeit in s',ylabel="v in m/s",title='Bahngeschwindigkeit')
#Bahnkurve
ax[0,1].plot(x, y,'k-',lw=1)
#ax[0,1].set_xticks([-2,0,2])
ax[0,1].set(xlabel='x in m',ylabel="y in m",title='Bahnkurve')
#Phasendiagramm
ax[1,1].plot(x, v,'g-',lw=1)
ax[1,1].set(xlabel='x',ylabel="v in m/s",title="Phasendiagramm")
fig.tight_layout()
print("Auslenkwinkel %2.2f in °" %np.degrees(phi0))
print("Masse der Kugel %3.2f kg"%m)
print("Periodendauer %3.2f s"%T)
print("Frequenz %3.2f Hz"%f)
print("Dämpfung %3.4f"%b)
print("maximale Geschwindigkeit %3.2f m/s"%vmax)
plt.show()

'''
#Foucaultsches Pendel 
d=1.896
l=67
phi=1.71 
'''



