#abb_11_13.py
#3D-Darstellung
import numpy as np
import matplotlib.pyplot as plt
#
def f(x,y):
    return 5-x-y
#
#fig, ax = plt.subplots(subplot_kw={"projection": "3d"},figsize=(8,8))
fig, ax = plt.subplots(subplot_kw={"projection": "3d"},figsize=(6,6))
x=np.arange(0, 2, 0.25)
y=np.arange(0, 2, 0.25)
x, y = np.meshgrid(x,y)
gw=1
ax.plot_wireframe(x,y,f(x,y),rstride=gw,cstride=gw,lw=2,color='r')
ax.set_xlim(0,2)
ax.set_ylim(0,2)
ax.set_zlim(0,5)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
#plt.tight_layout()
ax.grid(True)
plt.show()



