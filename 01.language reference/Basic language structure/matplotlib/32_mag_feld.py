#32_mag_feld.py
import numpy as np
import matplotlib as mlt
import matplotlib.pyplot as plt
x1,x2=0,12
y1,y2=0,7
x=np.linspace(1,9,9)
y=np.linspace(1,6,6)
x,y=np.meshgrid(x,y)
fig,ax=plt.subplots()
ax.axis([x1,x2,y1,y2])
stab=mlt.patches.Rectangle((1.4,0.25),0.2,6.5,color='black')#Breite,Höhe
kreis=mlt.patches.Circle((10,3.5),0.8,fill=False,lw=2,edgecolor='black')
ax.add_patch(kreis)
ax.add_patch(stab)
ax.plot([1,10],[6.5,6.5],lw=2,color='black')#obere Linie
ax.plot([1,10],[0.5,0.5],lw=2,color='black')#untere Linie
ax.plot([10,10],[0.5,6.5],lw=2,color='black')#rechte Linie
ax.plot(x,y,marker='x',color='red',ls='none')#magnetische Feldlinien
ax.arrow(1.6,3.5,1,0,color='k',lw=2,head_width=0.15)#Pfeile: x,y,x+dx,y+dy
ax.arrow(11,6,0,-4.5,color='b',lw=2,head_width=0.16,head_length=0.5)
ax.annotate("v",xy=(3,3),xytext=(3,3.4),fontsize=12)#Beschriftungen
ax.annotate("$U_q$",xy=(11.2,3),xytext=(11.3,3.2),fontsize=12)
ax.set_xticks([])#keine Achsenbeschriftung
ax.set_yticks([])#keine Achsenbeschriftung
ax.set_frame_on(False)
ax.set_aspect('equal')
plt.show()
'''
ax.set_axis_off() #Alternative für Zeile 26
'''