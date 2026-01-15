#10_sld_extremwerte.py
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
#Polynom
def f(x):
    return -x**3/4 + 3*x - 4
#zentraler Differenzenquotient
def ableitung(f,x,h=1e-3):
    return (f(x+h)-f(x-h))/(2*h)
#Tangentengleichung
def tangente(x,x0):
    m=ableitung(f,x0)
    return m*(x-x0)+f(x0)
#Slider-Einstellung ermitteln
def update(val):
    x0 = sldA.val
    m=ableitung(f,x0)
    xs=np.array([x0])
    y1.set_data(x,f(x))
    y2.set_data(x,tangente(x,x0))
    y3.set_data(xs,f(xs))
    txtM.set_text('m = %2.1f' %m)
#Grafikbereich
fig, ax = plt.subplots(figsize=(6,6))
ax.set_title("Polynom 3. Grades")
ax.set(xlabel="x",ylabel="y, y'")
ax.axis([-5,4,-10,4])
txtM=ax.text(0,3.2,'m=0')
x = np.linspace(-5, 4, 100)
y1,y2 = ax.plot(x, f(x),'g-', x, tangente(x,2),'b-',lw=1.5)
y3, = ax.plot(2,f(2), 'or') #Punkt
fig.subplots_adjust(left=0.12,bottom=0.2)
#x-, y-Position, Laenge, Hoehe
xyA = fig.add_axes([0.1, 0.05, 0.8, 0.03])
sldA=Slider(xyA,r'$x_0$',-5,4,valinit=1.2,valstep=0.1)
sldA.on_changed(update)
ax.grid(True)
plt.show()

'''
fig.savefig("/Users/veit/documents/Python_Mathe/Export_Mathe_Python_neu/Abbildungen/09_007.pdf")
fig.savefig("/Users/veit/documents/Python_Mathe/Export_Mathe_Python_neu/Abbildungen/09_007.svg")
'''

#y=6*np.sin(x)-3