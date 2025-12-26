#10_konstante_integrieren1.py
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integral
C=1 #F
imax=10
#Konstantstromquelle
@np.vectorize
def i(t):
    return imax
#Kondensatorspannung
@np.vectorize
def u(t):
    uc=(1/C)*integral.quad(i,0,t)[0]
    return uc

x = np.linspace(0, 20, 500)
fig, (ax1,ax2)=plt.subplots(2,1)
ax1.plot(x, i(x), 'r-', lw=2)
ax1.set(ylabel='Strom in A',title='Spannung am Kondensator')
ax2.plot(x, u(x),'b-',lw=2)
ax2.set(xlabel='t in s',ylabel='$u_c(t)$ in V')
ax1.grid(True);ax2.grid(True)
plt.show()

