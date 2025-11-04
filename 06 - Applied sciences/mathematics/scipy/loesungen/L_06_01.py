#L_06_01.py
import numpy as np
import matplotlib.pyplot as plt
from numdifftools import Derivative
L=1     #H
T=20    #ms
imax=1  #Ampere
#Dreieck: eingeprägter Strom
@np.vectorize
def i(t):
    m=2*imax/T
    if t < T/2:
        return m*t
    else:
        return -m*(t-T/2)+m*T/2
#induktiver Spannungsfall
def u(t):
    df=Derivative(i)
    return 1e3*L*df(t)

t = np.linspace(0,T,500)

fig,ax=plt.subplots(2,1)
ax[0].set_title("eingeprägter Strom")
ax[0].plot(t, i(t), color="r", lw=2)
ax[0].set_ylabel('Strom in A')
ax[0].grid(True)
#induktiver Spannungsfall
ax[1].set_title("induktiver Spannungsfall")
ax[1].plot(t, u(t), color="b",lw=2)
ax[1].set_xlabel('t ms')
ax[1].set_ylabel('Spannug in V')
ax[1].grid(True)
fig.tight_layout()
plt.show()


    
