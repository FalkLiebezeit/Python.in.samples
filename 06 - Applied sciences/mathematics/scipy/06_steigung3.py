#06_steigung3.py
import numpy as np
import matplotlib.pyplot as plt
from numdifftools import Derivative
L=1    #H
f=50   #Frequenz in Hz
omega=2*np.pi*f #1/s
imax=1. #A
#Stromquelle
def i(t):
    return imax*np.sin(omega*t*1e-3) #t in ms!
#induktiver Spannungsfall
def u(t):
    df=Derivative(i)
    return 1e3*L*df(t)

t = np.linspace(0,20,500) #ms
fig,(ax1,ax2)=plt.subplots(2,1)
ax1.plot(t, i(t), 'r-', lw=2)
ax1.set(ylabel='Strom in A',title='eingeprägter Strom')
ax1.grid(True)
#induktiver Spannungsfall
ax2.plot(t, u(t), 'b-',lw=2)
ax2.set(xlabel='t ms',ylabel='Spannug in V',title='induktiver Spannungsfall')
ax2.grid(True)
fig.tight_layout()
plt.show()

