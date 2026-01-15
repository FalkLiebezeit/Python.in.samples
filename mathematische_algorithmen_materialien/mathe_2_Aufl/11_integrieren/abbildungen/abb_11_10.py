#abb_11_10.py
#Rotationsparaboloid
import numpy as np
import matplotlib.pyplot as plt
#
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
u = np.arange(0, 2*np.pi, 0.25)
v = np.arange(0, 2*np.pi, 0.25)
u, v = np.meshgrid(u, v)
x=np.sqrt(u)*np.cos(v)
y=np.sqrt(u)*np.sin(v)
z=u
gw=2
h=(-1.5,1.5)
ax.plot_wireframe(z,y,x,rstride=gw,cstride=gw,lw=1,color='r')
ax.set_xlim( 1.5,6.8)
ax.set_ylim(h)
ax.set_zlim(h)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.axis('off')
ax.grid(False)
fig.tight_layout()
#ax.set_aspect('auto')
plt.show()


