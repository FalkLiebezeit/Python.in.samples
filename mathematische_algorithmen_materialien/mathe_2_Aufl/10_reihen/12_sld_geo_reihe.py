#12_sld_geo_reihe.py
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
#geometrische Reihe
def f(n,a,q):
    if q==1:
        q=1e-6
    return a*(q**(n+1)-1)/(q-1)
#Slider-Werte auslesen
def update(val):
    a = sldA.val
    q = sldB.val
    y.set_data(n,f(n,a,q))
    ax.relim()
    ax.autoscale_view()
    fig.canvas.draw_idle()
#Grafikbereich
fig, ax = plt.subplots()
fig.subplots_adjust(left=0.12, bottom=0.25)
ax.set_title(r'$s_{n}=a\frac{q^{n+1}-1}{q-1}$')
ax.set_xlim(0,11)
ax.set(xlabel='n',ylabel='$s_{n}$')
n = np.arange(0,11,1)
y, = ax.plot(n,f(n,1,0.5),'rx')
#x-, y-Position, Laenge, Hoehe
xyA = fig.add_axes([0.1, 0.10, 0.8, 0.03])
xyB = fig.add_axes([0.1, 0.05, 0.8, 0.03])
#Slider Objekte erzeugen
sldA=Slider(xyA,'a',0.5,4.0,valinit=1,valstep=0.1)
sldB=Slider(xyB,'q',-0.8,1.1,valinit= 0.5,valstep=0.01)
#Aenderungen abfragen
sldA.on_changed(update)
sldB.on_changed(update)
ax.grid(True)
plt.show()

