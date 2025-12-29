#L_04_18.py
'''Erde und Mars bewegen sich um die Sonne'''
import numpy as np
import matplotlib as mlt
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
#Daten
phi0=30
a1,b1=14,10 #innerer Planet
a2,b2=18,15 #außerer Planet
w1=0.02     #innerer Planet
w2=0.01     #außerer Planet
breite=20
#Funktionsdefinitionen
def init():
    erde.center = (0,0)
    mars.center = (0,0)
    ax.add_patch(erde)
    ax.add_patch(mars)
    return erde,mars

def planeten(t):
    phi1 = w1*t
    phi2 = w2*t + np.pi/4
    x1 = a1*np.sin(phi1)
    y1 = b1*np.cos(phi1)
    x2 = a2*np.sin(phi2)
    y2 = b2*np.cos(phi2)
    erde.center = (x1,y1)
    mars.center = (x2,y2)
    return erde,mars
#Grafikbereich
fig, ax = plt.subplots()
ax.axis([-breite, breite,-breite,breite])
sonne= mlt.patches.Circle((0,0),radius=2.0,color='y')
ax.add_artist(sonne)
erde = mlt.patches.Circle((0,0),radius=0.8, color='b')
mars = mlt.patches.Circle((0,0),radius=0.4, color='r')
#Animation
t=np.linspace(0,100,500)
anim = FuncAnimation(fig,planeten, 
                        init_func=init, 
                        #frames=t, 
                        interval=20,
                        blit=True,
                        save_count=50
                     )
ax.set_aspect('equal')
plt.show()