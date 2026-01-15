#L_11_01.py
#Fläche unter einer Kosinusfunktion
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
#Kosinus
def f(x):
    return np.cos(x)
#Stammfunktion
def F(x):
    return np.sin(x)
#
def update(val):
    a,b = sldA.val,sldB.val
    fx.set_data(x,f(x))
    pa.set_data([a],[f(a)]) #Punkt, links
    pb.set_data([b],[f(b)]) #Punkt, rechts
    va.set_data([a],[0,f(a)]) #verikale Linie, links
    vb.set_data([b],[0,f(b)]) #verikale Linie, rechts
    A=F(b)-F(a)
    txtA.set_text(f'A = {A:2.3f}')
#Grafikbereich
fig, ax = plt.subplots(figsize=(6,6),label="Fläche unter einer Kosinusfunktion")
ax.set(xlabel='x',ylabel='y')
fig.subplots_adjust(left=0.12,bottom=0.22)
ax.set_xlim(-np.pi/2,np.pi/2)
ax.set_ylim(0,1.5)
x = np.arange(-5,5,0.001)
fx, = ax.plot(x,f(x),color='b',lw=2)
x0=np.pi/2
pa,pb = ax.plot(-x0,f(x0),'ro',x0,f(x0),'ro')    #Grenzpunkte
va,vb = ax.plot([],[],[],[],color='k',lw=1) #vertikale Linien
txtA=ax.text(-0.2,1.2,'A=5.333') #Text
#x-, y-Position, Laenge, Hoehe
xyA = fig.add_axes([0.1, 0.10, 0.8, 0.03])
xyB = fig.add_axes([0.1, 0.05, 0.8, 0.03])
sldA=Slider(xyA,'a', -1.5, 0,valinit=-2,valstep=0.1)
sldB=Slider(xyB,'b', 0,1.5,valinit= 2,valstep=0.1)
sldA.on_changed(update)
sldB.on_changed(update)
ax.grid(True)
plt.show()



