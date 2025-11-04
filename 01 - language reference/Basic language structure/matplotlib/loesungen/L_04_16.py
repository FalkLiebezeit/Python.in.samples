##L_04_16.py
'''Ueberlagerung von zwei Sinusfunktionen'''
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
A1=4
A2=4
v=0.01
x1,x2=0,4*np.pi
y1,y2=-10,10
#1. Welle
def f1(t):
    return A1*np.sin(x + v*t)
#2. Welle
def f2(t):
    return A2*np.sin(x - v*t)
#fuer Animation
def w(t):
    y1.set_data(x,f1(t))
    y2.set_data(x,f2(t))
    y3.set_data(x,f1(t)+f2(t))
    return y1,y2,y3
#Grafikbereich
fig,ax = plt.subplots()#Objekte erzeugen
ax.axis([x1, x2,y1, y2])#Zeichenbereich
x = np.linspace(0, x2, 500)
y1, = ax.plot(x, f1(x),'r-')
y2, = ax.plot(x, f2(x),'b-')
y3, = ax.plot(x,f1(x) + f2(x),'k-.')
#Animation durchfuehren
a = FuncAnimation(fig,w,interval=20,blit=True,save_count=50)
ax.set(xlabel='x',ylabel='y')
plt.show()