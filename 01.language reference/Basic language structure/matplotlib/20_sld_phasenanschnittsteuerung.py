#20_sld_phasenanschnittsteuerung.py
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
Us=325     #Spitzenwert in V, 
a0=np.pi/4 #Anfangswert 45°
xmax=np.pi
#u(x), x ist ein Winkel
def u(x):
    return Us*np.sin(x)
#Slider abfragen
def update(val):
    alpha = sldAlpha.val #Steuerwinkel in°
    a=np.radians(alpha)  #Steuerwinkel in rad
    x = np.arange(a,xmax,0.01)
    y.set_data(x,u(x))
    linie.set_data([a,a],[u(0),u(a)])
    Uav=Us*(1.0 + np.cos(a))/np.pi
    txtWinkel.set_text(r'$\alpha$ = %.2f °' %alpha)
    txtUav.set_text(r'$U_{av}$ = %.2f V' %Uav)
#Grafikbereich
fig, ax = plt.subplots()
txtWinkel=ax.text(0.1,1.12*Us,r'$\alpha$ = %.2f °' %45)
txtUav=ax.text(0.1,1.05*Us,r'$U_{av}$ = 176.60 V')
fig.subplots_adjust(left=0.12,bottom=0.15)
ax.set_xlim(0,xmax)
ax.set_ylim(0,1.2*Us)
x0 = np.arange(a0,xmax,0.01) #für Anfangswerte
linie, = ax.plot([a0,a0],[u(0),u(a0)],'b-')
y, = ax.plot(x0,u(x0),'b-')
xyAlpha = fig.add_axes([0.1, 0.02, 0.8, 0.03])
sldAlpha=Slider(xyAlpha,r'$\alpha$',0,180,valinit=np.degrees(a0),valstep=1)
sldAlpha.on_changed(update)
ax.set(xlabel=r'$\alpha \  in\  rad$',ylabel='U in V')
secax = ax.secondary_xaxis('top',functions=(lambda x:10*x/np.pi,lambda x:np.pi*x))
secax.set_xlabel('t in ms')
plt.show()

'''
#Alternativen
def rad2time(x):return 10*x/np.pi
def time2rad(x):return np.pi*x
#secax = ax.secondary_xaxis('top', functions=(rad2time,time2rad))
secax = ax.secondary_xaxis('top',functions=(np.degrees,np.radians))
secax.set_xlabel('Winkel in °')
'''
'''
fig.savefig('04_018a.png')
fig.savefig('04_018a.svg')
'''

