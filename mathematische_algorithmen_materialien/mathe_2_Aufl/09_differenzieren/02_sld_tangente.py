#02_sld_tangente.py
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
#Funktionsdefinition
def f(x):
    return x**2/2
#1. Ableitung
def ableitung(f,x,h=1e-3):
    return (f(x+h)-f(x))/h
#Tangente
def tangente(x,x0):
    m=ableitung(f,x0)
    return m*(x-x0)+f(x0)
#Slider-Einstellung erfassen
def update(val):
    x0 = sldA.val
    m=ableitung(f,x0)
    y1.set_data(x,f(x))
    y2.set_data(x,tangente(x,x0))
    y3.set_data([x0],[f(x0)])
    txtM.set_text('m = %2.1f' %m)
#Grafikbereich
fig, ax = plt.subplots(figsize=(6,6),label='Steigung der Tangente')
ax.set_title(r'$y=\frac{1}{2} x^{2}$')
ax.set(xlabel='x',ylabel="y, y'")
ax.axis([-5,5,-0.25,12.5])
txtM=ax.text(0.05,11,'m=2.0')
x = np.linspace(-5.5, 5.5, 100)
y1,y2 = ax.plot(x, f(x),'g-', x, tangente(x,2),'b',lw=1.5)
y3, = ax.plot(2,f(2), 'or')
fig.subplots_adjust(left=0.12,bottom=0.2)
#x-, y-Position, Laenge, Hoehe
xyA = fig.add_axes([0.1, 0.05, 0.8, 0.03])
sldA=Slider(xyA,'$x_0$',-5,5.0,valinit=2,valstep=0.1)
sldA.on_changed(update)
ax.grid(True)
plt.show()

'''
fig.savefig("/Users/veit/documents/Python_Mathe/Export_Mathe_Python_neu/Abbildungen/09_003.pdf")
fig.savefig("/Users/veit/documents/Python_Mathe/Export_Mathe_Python_neu/Abbildungen/09_003.svg")
'''
