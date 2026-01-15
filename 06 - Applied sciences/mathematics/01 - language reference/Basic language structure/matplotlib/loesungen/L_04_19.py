#L_04_19.py
'''Mond-Erde-Sonne Rotationssystem'''
import numpy as np
import matplotlib as mlt
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
#Daten
phi0=30
a1,b1=14,10 #Erde
a2,b2=3,3   #Mond
w1=0.02     #Erde
w2=0.05     #Mond
breite=20
#Funktionsdefinitionen
def init():
    erde.center = (0,0)
    mond.center = (0,0)
    ax.add_patch(erde)
    ax.add_patch(mond)
    return erde,mond

def mond_erde(t):
    phi1 = w1*t
    phi2 = w2*t + np.pi/4
    x1 = a1*np.sin(phi1)
    y1 = b1*np.cos(phi1)
    x2 = a2*np.sin(phi2)
    y2 = b2*np.cos(phi2)
    erde.center = (x1,y1)
    mond.center = (x1+x2,y1+y2)
    return erde,mond
#Grafikbereich
fig, ax = plt.subplots(figsize=(6,6))
ax.axis([-breite, breite,-breite,breite])
sonne= mlt.patches.Circle((0,0),radius=2.0,color='y')
ax.add_artist(sonne)
erde = mlt.patches.Circle((0,0),radius=0.8, color='b')
mond= mlt.patches.Circle((0,0),radius=0.4, color='r')
#Animation
t=np.linspace(0,100,1000)
anim = FuncAnimation(fig,mond_erde, 
                    init_func=init, 
                    #frames=t, 
                    interval=100,
                    blit=True,
                    save_count=500
                     )
ax.set_aspect('equal')
plt.show()
