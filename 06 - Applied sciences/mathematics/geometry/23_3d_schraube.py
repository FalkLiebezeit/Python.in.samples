#22_3d_schraube.py
import numpy as np
import matplotlib.pyplot as plt
R=6
v0=5
omega=3
t=np.linspace(0,2*np.pi,500)
x=R*np.cos(omega*t)
y=R*np.sin(omega*t)
z=v0*t
ax = plt.figure(figsize=(6,6)).add_subplot(projection='3d')
ax.plot(x,y,z,lw=2)
ax.set(xlabel='x',ylabel='y',zlabel='z',title='Elektron im Magnetfeld')
plt.show()