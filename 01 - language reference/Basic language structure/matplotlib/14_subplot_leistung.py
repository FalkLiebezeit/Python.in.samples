#14_subplot_leistung.py
import numpy as np
import matplotlib.pyplot as plt
f=50
URms=230
R=0.001
Xc=10
XL=0
Z= np.sqrt(R**2 + (XL-Xc)**2)
phi=np.arctan((XL-Xc)/R)
I=URms/Z
t = np.linspace(0.0, 20, 1000)
u=np.sqrt(2)*URms*np.sin(2*np.pi*f*t*1e-3)
i=np.sqrt(2)*I*np.sin(2*np.pi*f*t*1e-3-phi)
p=u*i
fig, ax = plt.subplots(3,1)
#Spannung
ax[0].plot(t, u,'b',lw=2)
ax[0].set_ylabel('u(t)')
ax[0].grid(True)
#Strom
ax[1].plot(t,i,'r',lw=2)
ax[1].set_ylabel('i(t)')
ax[1].grid(True)
#Leistung
ax[2].plot(t,p,'g',lw=2)
ax[2].set(xlabel='Zeit in ms',ylabel='p(t)')
ax[2].grid(True)
fig.tight_layout()
plt.show()