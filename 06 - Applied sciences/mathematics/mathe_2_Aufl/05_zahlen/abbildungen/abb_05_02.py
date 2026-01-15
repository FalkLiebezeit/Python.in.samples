#abb_05_02.py
import matplotlib.pyplot as plt
from matplotlib import patches
fig, ax = plt.subplots(figsize=(10,2))
#x1,x2,y1,y2
plt.axis([-1,18,-1,2])
r1 = patches.Rectangle((0,0), 17, 1,fill=False,lw=2,color='b')
#Ursprung x,y,dx,dy,breite
ax.arrow(9,-0.5,7.8,0,fill=True,width=0.01,head_length=0.2,head_width=0.15,color='k')
ax.arrow(8,-0.5,-7.8,0,fill=True,width=0.01,head_length=0.2,head_width=0.15,color='k')
ax.vlines(5,0,1,color='r')
ax.vlines(10,0,1,color='r')
ax.vlines(15,0,1,color='r')
plt.text(2.5,0.3,"5",fontsize='12')
ax.text(7.5,0.3,"5",fontsize='12')
ax.text(12.5,0.3,"5",fontsize='12')
ax.text(15.8,0.3,"2",fontsize='12')
ax.text(8.3,-0.6,"17",fontsize='12')
ax.add_patch(r1)
ax.axis('off')
fig.tight_layout()
plt.show()