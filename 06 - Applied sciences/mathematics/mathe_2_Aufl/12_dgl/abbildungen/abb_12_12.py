#abb_12_12.py
#Federpendel, waagerecht
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
#
fig, ax = plt.subplots(figsize=(6,3))
#x1,x2,y1,y2
ax.axis([-1,81,-0.1,5])
#x1,y1,x2,y2
wand = Rectangle((0,1),2,4,fill=True,lw=2,color='gray')
boden = Rectangle((0,0.70),75,0.25,fill=True,lw=2,color='gray')
masse = Rectangle((33.7,1),15,2,fill=False,lw=2,color='b')
l=10
#Feder
x=np.linspace(0,10*np.pi,500)
y=0.5*np.sin(x)+2
ax.plot(x+2.3,y,color='black')
#x,y1,y2
plt.vlines(41,3.1,4)
#Ursprung x,y,dx,dy,breite
ax.text(34,4.3,"Ruhelage",color='r',fontsize='14')
ax.text(39.5,1.8,"m",color='r',fontsize='14')
ax.text(55,2.15,r"$F_{s}$",color='r',fontsize='14')
ax.text(74,-0.5,"x",color='r',fontsize='14')
ax.text(15,3,"c",color='r',fontsize='14')

ax.add_patch(wand)
ax.add_patch(boden)
ax.add_patch(masse)
#x,y,dx,dy
ax.arrow(48.8,2,12,0,head_width=0.2,head_length=1.8)
ax.arrow(0,0,74,0,lw=0.8,head_width=0.2,head_length=1.8)
ax.axis('off')
fig.tight_layout()
plt.show()
