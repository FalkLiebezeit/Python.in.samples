#L_04_20.py
'''
schwingende Saite
y(x,t)=[2*ym*sin(k*x)]*cos(w*t)
Halliday S. 483
'''
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
k=1
x1,x2=0, np.pi
y1,y2=-10, 10
#Funktionsdefinitionen
def f(t,k):
    w=0.1
    y=8*np.sin(k*x)*np.cos(w*t)
    return y
#Aenderung der Amplitude    
def saite(t):
    y=f(t,k)
    line.set_ydata(y)
    return line,
#Grafikbereich
fig, ax = plt.subplots()
ax.axis([x1,x2,y1,y2])
x = np.arange(x1,x2, 0.01)
line, = ax.plot(x,f(x,1))
ax.plot(x1,0,'ro',ms=10) #Aufhaengung
ax.plot(x2,0,'ro',ms=10)

ani = FuncAnimation(fig, saite,
                    #frames=1000, 
                    interval=20, 
                    blit=True, 
                    save_count=50
                    )
ax.set(xlabel='x',ylabel='y')
plt.show()
