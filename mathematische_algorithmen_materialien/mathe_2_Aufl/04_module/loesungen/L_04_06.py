#L_04_06.py
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
#Funktionsdefinition
def f(x,a,b,c):
    return a*x**2+b*x+c
#Slider-Einstellungen erfassen
def update(val):
    a = sldA.val
    b = sldB.val
    c = sldC.val
    y.set_data(x,f(x,a,b,c))
    fig.canvas.draw_idle()
#Grafikbereich
fig, ax = plt.subplots(figsize=(6,6),label='Parabel')
ax.set_title(r'$y=a_{2}x^{2}+a_{1}x+a_{0}$')
ax.set(xlabel='x',ylabel='y')
ax.axis([-5.5,5.5,-10,10])
fig.subplots_adjust(left=0.12,bottom=0.25)
x = np.arange(-5.5,5.5,0.001)
y, = ax.plot(x,f(x,1,0,-10),lw=2)
#x-, y-Position, Breite, Höhe
xyA = fig.add_axes([0.1, 0.10, 0.8, 0.03])
xyB = fig.add_axes([0.1, 0.05, 0.8, 0.03])
xyC = fig.add_axes([0.1, 0.00, 0.8, 0.03])
#Slider Objekte erzeugen
sldA=Slider(xyA,'$a_2$', -2.0, 2.0,valinit=1, valstep=0.1)
sldB=Slider(xyB,'$a_1$', -5.0, 5.0,valinit=0, valstep=0.1)
sldC=Slider(xyC,'$a_0$',-10.0,10.0,valinit=-10,valstep=0.1)
#Änderungen ausführen
sldA.on_changed(update)
sldB.on_changed(update)
sldC.on_changed(update)
ax.grid(True)
plt.show()



