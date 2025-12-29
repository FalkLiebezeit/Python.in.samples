#06_steigung3_alt.py
import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import derivative
L=1    #H
f=50   #Frequenz in Hz
omega=2*np.pi*f
imax=1. #A
#Stromquelle
def i(t):
    return imax*np.sin(omega*t/1e3)
#induktiver Spannungsfall
def u(t):
    return 1e3*L*derivative(i,t,dx=1e-6)

t = np.linspace(0,20,500)
fig,(ax1,ax2)=plt.subplots(2,1)
ax1.set_title("eingeprägter Strom")
ax1.plot(t, i(t), color="r", lw=2)
ax1.set_ylabel('Strom in A')
ax1.grid(True)
#induktiver Spannungsfall
ax2.set_title("induktiver Spannungsfall")
ax2.plot(t, u(t), color="b",lw=2)
ax2.set_xlabel('t ms')
ax2.set_ylabel('Spannug in V')
ax2.grid(True)
fig.tight_layout()
plt.show()
