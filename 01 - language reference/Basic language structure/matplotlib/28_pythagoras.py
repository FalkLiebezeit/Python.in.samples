#28_pythagoras.py
import numpy as np
import matplotlib as mlt
import matplotlib.pyplot as plt
x1,x2=-3,8
y1,y2=-1,11
a,b=3,4
alpha=np.degrees(np.arctan(b/a))
beta=90-np.degrees(np.arctan(a/b))
c=np.hypot(a,b)
fig,ax=plt.subplots()
ax.axis([x1,x2,y1,y2])
#(x1,y1),Breite,Höhe
ra=mlt.patches.Rectangle((0,c),a,a,fill=False,lw=2,edgecolor='b',angle=alpha)
rb=mlt.patches.Rectangle((c,c),b,b,fill=False,lw=2,edgecolor='b',angle=beta)
rc=mlt.patches.Rectangle((0,0),c,c,fill=False,lw=2,edgecolor='b')
ax.add_patch(ra)
ax.add_patch(rb)
ax.add_patch(rc)
ax.set_aspect('equal')
ax.set_xticks([])
ax.set_yticks([])
ax.set_frame_on(False)
plt.show()
'''
ax.set_axis_off() #Alternative für Zeile 23
'''