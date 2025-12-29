#07_steigung4.py
import numpy as np
import matplotlib.pyplot as plt
from numdifftools import Derivative
g=9.81
#Weg
def s(t):
    return g*t**2/2
#Geschwindigkeit
def v(t):
    df=Derivative(s,n=1)
    return df(t)
#Beschleunigung
def a(t):
    df=Derivative(v,n=1)
    return df(t)
#Zeit
t = np.linspace(0,5,100) #Sekunden
fig,ax =plt.subplots(3,1,figsize=(6,6))
#Weg
ax[0].plot(t, s(t), 'b-', lw=2)
ax[0].set(ylabel='s in m',title='Weg')
#Geschwindigkeit
ax[1].plot(t, v(t), 'r-', lw=2)
ax[1].set(ylabel='v in m/s',title='Geschwindigkeit')
#Beschleunigung
ax[2].plot(t, a(t), 'g-', lw=2)
ax[2].set(xlabel='t in s',ylabel='a',title='Beschleunigung')
ax[2].set_ylim(0,12)
[ax[i].grid(True) for i in range(len(ax))]
fig.tight_layout()
plt.show()
# fig.savefig('weg_zeit.png')
# fig.savefig('weg_zeit.svg')
