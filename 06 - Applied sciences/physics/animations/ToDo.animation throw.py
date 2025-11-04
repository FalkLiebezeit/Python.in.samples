#34_animation_wurf.py
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
g=9.81
v0=10          #Anfangsgeschwindigkeit in m/s
wurfwinkel=45  #Abwurfwinkel in °
alpha=np.radians(wurfwinkel)
tmax=2*v0*np.sin(alpha)/g
xmax=v0**2*np.sin(2*alpha)/g
ymax=v0**2*np.sin(alpha)**2/(2*g)
#Wurfbahn berechnen
def wurf(t):
    x=v0*np.cos(alpha)*t
    y=v0*np.sin(alpha)*t-0.5*g*t**2
    #ball.set_data([x],[y])
    ball.set_data(x,y)
    return ball,
#Objekte erzeugen
fig,ax=plt.subplots()
ax.axis([0,xmax+0.5,0,ymax+0.5])
ball, = ax.plot([],[],'ro')
t=np.linspace(0,tmax,100)
ani=FuncAnimation(fig,wurf,frames=t,interval=20,blit=True)
ax.set(xlabel="x in m",ylabel="y in m",title="Schiefer Wurf")
plt.show()
'''
#in Zeile 25 einfügen
markersize='15' #Ball vergrößern
#für Initialisierung
def init():
    ax.axis([0,xmax+0.5,0,ymax+0.5])
    ball.set_data([], [])
    return ball,
'''
#ball.set_data(x,y) #zum testen in Zeile 16