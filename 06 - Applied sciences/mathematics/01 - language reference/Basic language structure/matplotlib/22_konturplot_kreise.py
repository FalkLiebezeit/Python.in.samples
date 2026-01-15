#22_konturplot_kreise.py
import numpy as np
import matplotlib.pyplot as plt
I=62.8 #Stromstärke
rmax=10
n=100
lev=[1,2,4,8,16]
x=y=np.linspace(-rmax,rmax,n)
x,y=np.meshgrid(x,y)
H=I/(2*np.pi*np.hypot(x,y))
fig,ax=plt.subplots()
cp=ax.contour(x,y,H,levels=lev,colors='red')
ax.clabel(cp,inline=True)
ax.set(xlabel='x',ylabel='y')
ax.set_aspect('equal')
plt.show()