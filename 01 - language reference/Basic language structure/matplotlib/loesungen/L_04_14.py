#L_04_14.py
'''Überlagerung von Schwingungen mit gleicher Frequenz'''
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
T=20
A=10
#feste Frequenz
def f1(t):
    T=20
    return A*np.cos(2*np.pi*t/T)
#Phasenverschiebung
def f2(t,phi):
    return A*np.cos(2*np.pi*t/T-phi)
#Änderungen abfragen
def update(val):
    phi=sldPhi.val
    phi=np.radians(phi)
    y1.set_data(t,f1(t))
    y2.set_data(t,f2(t,phi)) 
    y3.set_data(t,f1(t)+f2(t,phi)) 
#Grafikbereich
fig, ax = plt.subplots(figsize=(6,6))
fig.subplots_adjust(left=0.13,bottom=0.12)
ax.set_xlim(0,20)
ax.set_ylim(-2*A,2*A)
ax.set_title('Überlagerung von Schwingungen')
ax.set_xlabel('t')
ax.set_ylabel('Amlitude')
y1, = ax.plot([],[],'b-',lw=1.5)
y2, = ax.plot([],[],'r-',lw=1.5)
y3, = ax.plot([],[],'g-',lw=2) 
#x-, y-Position, Laenge, Hoehe
# xyA = fig.add_axes([0.1, 0.09, 0.8, 0.03])
# xyDelta = fig.add_axes([0.1, 0.05, 0.8, 0.03])
xyPhi= fig.add_axes([0.1, 0.01,  0.8, 0.03])
#Slider Objekte erzeugen
# sldA=Slider(xyA,r'$A$',0,10, valinit=10,valstep=1)  #Amplitude
# sldDelta=Slider(xyDelta,r'$\delta$',0.0,1.1, valinit=0.2,valstep=0.01)#Dämpfung
sldPhi=Slider(xyPhi,r'$\varphi$',0,180, valinit=5.0,valstep=0.01) #Periodendauer
t=np.linspace(0,20,200)
#Änderungen durchfuehren
# sldA.on_changed(update)
# sldDelta.on_changed(update)
sldPhi.on_changed(update)
plt.show()




