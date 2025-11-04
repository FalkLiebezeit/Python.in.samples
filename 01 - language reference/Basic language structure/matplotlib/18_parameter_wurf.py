#16_parameter_wurf.py
import numpy as np
import matplotlib.pyplot as plt
g=9.81
v0=20
alpha=45
alpha=np.radians(alpha)
tmax=2*v0*np.sin(alpha)/g
t=np.linspace(0,tmax,100)
#Parametergleichungen
x=v0*np.cos(alpha)*t
y=v0*np.sin(alpha)*t-0.5*g*t**2
#Darstellung
fig, ax=plt.subplots()
ax.plot(x,y,linewidth=2)
ax.set(xlabel='x in m',ylabel='y in m')
ax.grid(True)
plt.show()