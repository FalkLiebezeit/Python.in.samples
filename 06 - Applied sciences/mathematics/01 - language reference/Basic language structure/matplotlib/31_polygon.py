#31_polygon.py
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import  Polygon
r=10
n=6
R=1.1*r
fig,ax=plt.subplots()
ax.axis([-R,R,-R,R])
for k in range(n):              
    w=2*np.pi/n         
    x1,y1=r*np.cos(k*w),r*np.sin(k*w)     
    x2,y2=r*np.cos((k+1)*w),r*np.sin((k+1)*w)  
    ax.plot([0,x2],[0,y2],lw=1,color='b')
    p=Polygon([[x1,y1],[x2,y2]],fill=False,lw=2)
    ax.add_patch(p)
ax.set_aspect('equal')
ax.grid(True)
plt.show()
