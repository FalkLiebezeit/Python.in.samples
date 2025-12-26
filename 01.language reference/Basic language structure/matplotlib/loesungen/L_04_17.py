#L_04_17.py
'''Punkt bewegt sich auf Sinuskurve'''
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
A=8 #Amplitude
xmax,ymax=2*np.pi,10
#Bahnkurve
def f(t):
    y= A*np.sin(t)
    #y=-(t - np.pi)**2
    return y
#Bahnberechnung für Punkt
def bahn(t):
    yp=f(t)
    zeit=t
    txtZeit.set_text('t = %.1f' %zeit)
    punkt.set_data([t],[yp])
    return punkt,txtZeit
#Objekte erzeugen
fig,ax=plt.subplots()
ax.axis([0,xmax,-ymax,ymax])
txtZeit=ax.text(0.2,9,'',fontsize=12)
punkt, = ax.plot([],[],'ro',ms=10) #roter Punkt
t=np.linspace(0,xmax,500)
ax.plot(t,f(t)) #Bahnkurve
ani=FuncAnimation(fig,bahn,frames=t,interval=20,blit=True)
ax.set(xlabel='x',ylabel='y')
plt.show()


