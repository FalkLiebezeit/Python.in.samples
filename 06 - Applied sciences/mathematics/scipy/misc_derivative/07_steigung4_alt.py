#07_steigung4_alt.py
import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import derivative
g=9.81
#Weg
def s(t):
    return g*t**2/2
#Geschwindigkeit
def v(t):
    return derivative(s,t)
#Beschleunigung
def a(t):
    return derivative(v,t,dx=2)

t = np.linspace(0, 5, 40)
#Weg
fig, ax =plt.subplots(3,1,figsize=(8,8))
ax[0].plot(t, s(t), 'b-', lw=2)
ax[0].set(ylabel='s in m',title='Weg')
#Geschwindigkeit
ax[1].plot(t, v(t),'r-', lw=2)
ax[1].set(ylabel='v in m/s',title='Geschwindigkeit')
#Beschleunigung
ax[2].plot(t, a(t), 'g-', lw=2)
ax[2].set(xlabel='t in s',ylabel='a',title='Beschleunigung')
[ax[i].grid(True) for i in range(len(ax))]
fig.tight_layout()
plt.show()