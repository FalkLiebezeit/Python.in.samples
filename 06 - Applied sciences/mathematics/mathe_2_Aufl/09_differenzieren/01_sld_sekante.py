#01_sld_sekante.py
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
#Funktionsdefinition
def f(x):
    return x**2/2
#Sekante
def sekante(x,x0=2,h=3):
    m=(f(x0+h)-f(x0))/h
    x0=x0-f(x0)/m
    return m*(x-x0)
#Slider-Wert auslesen
def update(val):
    x0=2
    h = sldA.val
    m=(f(x0+h)-f(x0))/h
    y1.set_data(x,f(x))
    y2.set_data(x,sekante(x,x0,h))
    y3.set_data([x0],[f(x0)])
    y4.set_data([x0+h],[f(x0+h)])
    txtM.set_text('m = %2.1f' %m)
#Grafikbereich
fig, ax = plt.subplots(figsize=(6,6),label='Grenzwertprozess')
ax.set_title(r"$y=\frac{1}{2} x^{2}$")
ax.set(xlabel="x",ylabel=r"$y, \frac{\Delta y}{\Delta x}$")
ax.axis([0,5.5,-0.25,13])
txtM=ax.text(0.06,11,'m=3.5')
x = np.linspace(0, 5.5, 100)
y1,y2 = ax.plot(x,f(x),"g-",x,sekante(x),"b-",lw=2.0)
y3,y4 = ax.plot(2,f(2),"ro",5,f(5),"ko") #Punkte
fig.subplots_adjust(left=0.12,bottom=0.2)
#x-, y-Position, Laenge, Hoehe
xyA = fig.add_axes([0.1, 0.05, 0.8, 0.03])
sldA=Slider(xyA,r'$\Delta x$',0.01,3,valinit=3,valstep=0.1)
sldA.on_changed(update)
ax.grid(True)
plt.show()

'''
fig.savefig("/Users/veit/documents/Python_Mathe/Export_Mathe_Python_neu/Abbildungen/09_002.pdf")
fig.savefig("/Users/veit/documents/Python_Mathe/Export_Mathe_Python_neu/Abbildungen/09_002.svg")
'''
