#01_sld_schnittpunkt.py
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
#1. Funktion
def f1(x,a=1,b=1):
    return a*x+b
#2. Funktion
def f2(x,c=-1,d=5):
    return c*x+d
#Slider-Einstellungen erfassen
def update(val):
    a = sldA.val
    b = sldB.val
    c = sldC.val
    d = sldD.val
    y1.set_data(x,f1(x,a,b))
    y2.set_data(x,f2(x,c,d))
    fig.canvas.draw_idle()
#Grafikbereich
fig, ax = plt.subplots(figsize=(6,6))
x = np.arange(-10,10,0.001)
y1,y2 = ax.plot(x,f1(x,1,1),x,f2(x,-1,5),lw=1.5)
ax.set_title(r'$y_{1}=ax+b,\  y_{2}=cx+d$')
ax.set_xlabel('x')
ax.set_ylabel('y',rotation=True)
ax.grid(True)
ax.set_xlim(-10,10)
ax.set_ylim(-10,10)
ax.set_xticks(np.arange(-10, 11, 1))
ax.set_yticks(np.arange(-10, 11, 1))
fig.subplots_adjust(left=0.12, bottom=0.26)
#x-, y-Position, Laenge, Hoehe der Slider
xyA = fig.add_axes([0.1, 0.15, 0.8, 0.03])
xyB = fig.add_axes([0.1, 0.10, 0.8, 0.03])
xyC = fig.add_axes([0.1, 0.05, 0.8, 0.03])
xyD = fig.add_axes([0.1, 0.00, 0.8, 0.03])
#Slider Objekte erzeugen
sldA=Slider(xyA,'a', -5.0, 5.0,valinit=1,valstep=0.1)
sldB=Slider(xyB,'b', -10.0, 10.0,valinit=1,valstep=0.1)
sldC=Slider(xyC,'c',-5.0,5.0,valinit=-1,valstep=0.1)
sldD=Slider(xyD,'d',-10.0,10.0,valinit=5,valstep=0.1)
#Änderungen abfragen
sldA.on_changed(update)
sldB.on_changed(update)
sldC.on_changed(update)
sldD.on_changed(update)
plt.show()

'''
fig.savefig("/Users/veit/documents/Python_Mathe/Dateien_fuer_Autor/Abbildungen/06_001.png")
'''