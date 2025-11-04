#L_04_15.py
'''Phasenabschittsteuerung'''
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
    y.set_data(x-a,u(x-a)) #Sinus
    linie.set_data([xmax-a,xmax-a],[u(0),u(xmax-a)]) #Phase
#Grafikbereich
fig, ax = plt.subplots()
fig.subplots_adjust(left=0.12,bottom=0.15)
ax.set_xlim(0,xmax)
ax.set_ylim(0,1.2*Us)
linie, = ax.plot([],[],'b-')
y, = ax.plot([],[],'b-')
xyAlpha = fig.add_axes([0.1, 0.02, 0.8, 0.03])
sldAlpha=Slider(xyAlpha,r'$\alpha$',0,180,valinit=np.degrees(a0),valstep=1)
sldAlpha.on_changed(update)
plt.show()



