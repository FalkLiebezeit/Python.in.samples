#L09_02.py
#Normale
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
#
def f(x):
    return 3*x**(1/2)
#
def ableitung(f,x,h=1e-3):
    return (f(x+h)-f(x-h))/(2*h)
#Normale
def fn(x,x0):
    m=ableitung(f,x0)
    if m==0:
        m=1e-6
    return -(x-x0)/m+f(x0)
#
def update(val):
    a = sldA.val
    y1.set_data(x,f(x))
    y2.set_data(x,fn(x,a))
    y3.set_data([a],[f(a)])
#Grafikbereich
fig, ax = plt.subplots(figsize=(6,6),label='Normale')
fig.subplots_adjust(left=0.12,bottom=0.2)
ax.set_title(r"$y=3\sqrt{x}$")
ax.set_xlabel("x")
ax.set_ylabel("y")
x2=16
ax.set_xlim(0,x2)
ax.set_ylim(-0.25,12.5)
x = np.linspace(0, x2, 200)
y1,y2 = plt.plot(x, f(x),'k-', x, fn(x,2),'b-')
y3, = plt.plot(2, f(2), 'ro')
#x-, y-Position, Laenge, Hoehe
xyA = fig.add_axes([0.1, 0.05, 0.8, 0.03])
sldA=Slider(xyA,'a',0.1,x2,valinit=2,valstep=0.1)
sldA.on_changed(update)
ax.grid(True)
ax.set_aspect('equal')
plt.show()


