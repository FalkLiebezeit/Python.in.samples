#11_konstante_integrieren2.py
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integral
g=9.81
@np.vectorize
def a(t): #Beschleunigung
    return g
@np.vectorize
def v(t): #Geschwindigkeit
    return integral.quad(a, 0, t)[0]
@np.vectorize
def s(t): #Weg
    return integral.quad(v, 0, t)[0]
#Zeit-Werte
t = np.linspace(0,5,100)
fig, ax=plt.subplots(3,1,figsize=(6,8))
ax[0].plot(t, a(t), 'g-', lw=2)
ax[0].set(ylabel='a in $m/s^2$',title='Beschleunigung')
ax[0].set_ylim(0,12)
ax[1].plot(t, v(t), 'r-',lw=2)
ax[1].set(ylabel='v in m/s',title='Geschwindigkeit')
ax[2].plot(t, s(t), 'b-', lw=2)
ax[2].set(xlabel='t in s',ylabel='s in m',title='Weg')
[ax[i].grid(True) for i in range(len(ax))]
fig.tight_layout()
plt.show()
# fig.savefig('06_014.png')
# fig.savefig('06_014.svg')