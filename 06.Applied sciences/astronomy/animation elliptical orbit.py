"""Simulation of a planetary orbit using Newtonian gravity.

Assumes the Sun is fixed at the origin.
The simulation uses a simple ODE solver and visualizes the planet's trajectory,
velocity, and acceleration vectors. Note: The numerical accuracy is limited,
so the orbit is not perfectly closed and the planet spirals inward over time.
"""

import numpy as np
import matplotlib as mlt
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#Daten
r1,r2=0.5,0.25   
a,b=8,4 #Ellipsenachsen
breite=10

#Initialisierung
def init():
    planet.center=(1,2)
    ax.add_patch(planet)
    return planet,
#Bahnberechnung
def bahn(t):
    x,y=a*np.cos(np.radians(t)),b*np.sin(np.radians(t)) 
    planet.center=(x,y)
    return planet,
#Grafikbereich
fig,ax=plt.subplots()
ax.axis([-breite,breite,-breite,breite])
planet= mlt.patches.Circle((0,0),  radius=r2, color='blue')
stern = mlt.patches.Circle((2.5,0),radius=r1, color='red')
ax.add_artist(stern)
ani=FuncAnimation(fig,bahn,init_func=init,frames=360,interval=20,blit=True)
ax.set_aspect('equal')
ax.set(xlabel='x',ylabel='y',title='elliptical orbit')
plt.show()
