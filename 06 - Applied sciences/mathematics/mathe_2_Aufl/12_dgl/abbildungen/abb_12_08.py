#abb_12_08.py
#gekoppeltes Fadenpendel
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
#
fig, ax = plt.subplots(figsize=(4,4))
#x1,x2,y1,y2
ax.axis([-5,100,-1,100])
#x1,y1,x2,y2
decke = mpatches.Rectangle((10,95),75,100,fill=True,lw=2,color='gray')
#x1,x2,y1,y2
ax.plot([10,30],[30,95],color='k',lw=2)
ax.plot([88,65],[27.8,95],color='k',lw=2)
ax.plot([30,30],[50,95],color='k',lw=1,ls='dashed')
ax.plot([65,65],[50,95],color='k',lw=1,ls='dashed')
# x,y, Radius
farbe='lightblue'
m1 = mpatches.Circle((8,20),10,color=farbe)
m2 = mpatches.Circle((90,18),10,color=farbe)
#Feder
x=np.linspace(0,20*np.pi,500)
y=5*np.sin(x)+20
ax.plot(x+17.5,y,color='black')
#Beschriftung
ax.text(22,56,r"$\varphi_{1} $",color='r',fontsize='14')
ax.text(69,56,r"$\varphi_{2} $",color='r',fontsize='14')
ax.text(50,30,"c",color='r',fontsize='14')
ax.text(5.5,19,r"$m$",color='black',fontsize='14')
ax.text(88,17,r"$m$",color='black',fontsize='14')
ax.text(11,50,r"$l$",color='black',fontsize='14')
ax.text(84,50,r"$l$",color='black',fontsize='14')

ax.add_patch(decke)
ax.add_patch(m1)
ax.add_patch(m2)
#x,y,dx,dy
# plt.arrow(48.8,2,12,0,head_width=0.2,head_length=1.8)
# plt.arrow(0,0,74,0,lw=0.8,head_width=0.2,head_length=1.8)
ax.axis('off')
ax.set_aspect('equal')
fig.tight_layout()
plt.show()

