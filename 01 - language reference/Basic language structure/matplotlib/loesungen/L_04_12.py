#L_04_12.py
'''Simulation einer gedaempften Schwingung'''
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
#gedaempfte Schwingung
def f(t,A,delta,T):
    return A*np.exp(-delta*t)*np.cos(2*np.pi*t/T)
#Änderungen abfragen
def update(val):
    A=sldA.val 
    delta=sldDelta.val
    T=sldT.val
    y.set_data(t,f(t,A,delta,T)) 
#Grafikbereich
fig, ax = plt.subplots(figsize=(6,6))
fig.subplots_adjust(left=0.13,bottom=0.2)
ax.set_xlim(0,20)
ax.set_ylim(-10,10)
ax.set_title('gedaempfte Schwingung')
ax.set_xlabel('t')
ax.set_ylabel('Amplitude')
y, = ax.plot([],[],'b-',lw=2) 
#x-, y-Position, Laenge, Hoehe
xyA = fig.add_axes([0.1, 0.09, 0.8, 0.03])
xyDelta = fig.add_axes([0.1, 0.05, 0.8, 0.03])
xyT= fig.add_axes([0.1, 0.01,  0.8, 0.03])
#Slider Objekte erzeugen
sldA=Slider(xyA,r'$A$',0,10, valinit=10,valstep=1)  #Amplitude
sldDelta=Slider(xyDelta,r'$\delta$',0.0,1.1, valinit=0.2,valstep=0.01)#Dämpfung
sldT=Slider(xyT,r'$T$',1,10, valinit=5.0,valstep=0.01) #Periodendauer
t=np.linspace(0,20,200)
#Änderungen durchfuehren
sldA.on_changed(update)
sldDelta.on_changed(update)
sldT.on_changed(update)
plt.show()



