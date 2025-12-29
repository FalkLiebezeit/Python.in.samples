#23_dgl_doppelpendel.py
import numpy as np
from numpy import sin,cos
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
g = 9.81    #Erdbeschleunigung in m/s^2
l1,l2 = 2,1 #Pendellaengen in m
m1,m2 = 5,1 #Pendelmassen in kg
phi1, phi2 = 120, -10 #Auslenkung
tmax=20     #Simulationsdauer in Sekunden
#DGL-System
def dgl(t,ya,l1, l2, m1, m2):
    phi1,w1,phi2,w2 = ya
    delta=phi2-phi1 #Abkuerzung fuer Winkel
    m=m1+m2         #Abkuerzung fuer Masse
    phi1_dt = w1 #1. Ableitung Winkel oben
    w1_dt=(m2*l1*w1**2*sin(delta)*cos(delta)\
           +m2*g*sin(phi2)*cos(delta)+m2*l2*w2**2*sin(delta)-m*g*sin(phi1))\
           /(m*l1-m2*l1*cos(delta)**2)
    phi2_dt = w2 #1. Ableitung Winkel unten
    w2_dt=(-m2*l2*w2**2*sin(delta)*cos(delta)\
           + m*(g*sin(phi1)*cos(delta)-l1*w1**2*sin(delta)-g*sin(phi2)))\
           /(m*l2-m2*l2*cos(delta)**2)
    return np.array([phi1_dt, w1_dt, phi2_dt, w2_dt])
#Lösung des DGL-Systems
omega1 = omega2 = 0
ya =[np.radians(phi1),omega1,np.radians(phi2),omega2]
t = np.linspace(0,tmax,500)
z=solve_ivp(dgl,[0,tmax],ya,args=(l1,l2,m1,m2),dense_output=True)
phi1, w1, phi2, w2 = z.sol(t) #Lösungen
#Berechnung der x,y-Koordinaten, l1 ist im Ursprung verankert
x1,y1 =    l1*sin(phi1),  -l1*cos(phi1) #1. Pendel 
x2,y2 = x1+l2*sin(phi2),y1-l2*cos(phi2) #2. Pendel
fig, ax = plt.subplot_mosaic([['upper left', 'right'],
                              ['lower left', 'right']],
                              figsize=(8,4), layout="constrained")
#Auslenkung Pendel l1 (oben)
breite=1.1*(l1+l2)
ax['upper left'].plot(t,x1,'r-',lw=1)#x-Richtung oben
ax['upper left'].plot(t,y1,'b-',lw=1)#y-Richtung oben
ax['upper left'].set(ylabel='$x_1, y_1$',title='Pendel 1')
#Auslenkung Pendel l2 (unten)
ax['lower left'].plot(t,x2,'r-',lw=1) #x-Richtung unten
ax['lower left'].plot(t,y2,'b-',lw=1) #y-Richtung unten
ax['lower left'].set(xlabel='t',ylabel='$x_2, y_2$',title='Pendel 2')
#Bahnkurven
breite=1.1*(l1+l2)
ax['right'].plot(x1,y1,'r-',lw=1,label='Pendel 1')
ax['right'].plot(x2,y2,'b-',lw=1,label='Pendel 2')
ax['right'].set(xlabel='x',ylabel='y',title='Bahnkurven')
ax['right'].legend(loc='best')
ax['right'].set_xlim(-breite,breite)
ax['right'].set_ylim(-breite,breite)
plt.show()
'''
Quelle für DGL-System:
http://www.physics.usyd.edu.au/~wheat/dpend_html/
'''
'''
ax['upper left'].text(1.2,1.7,'$x_1$',color='red')
ax['upper left'].text(-0.6,-1.7,'$y_1$',color='blue')
return [phi1_dt, w1_dt, phi2_dt, w2_dt]
fig.savefig('doppelpendel.png')
fig.savefig('doppelpendel.svg')
'''

