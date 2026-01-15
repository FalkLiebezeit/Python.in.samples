#03_003.py
#Namensraum
import matplotlib.pyplot as plt
from matplotlib import patches
#
fig, ax = plt.subplots(figsize=(6,3))
#x1,x2,y1,y2
ax.axis([-5,5,-1,12])
l=2
#x,y, width, height
r1 = patches.Rectangle((-2,0),4,9,fill=True,lw=1,color='k',alpha=0.1) #außen
r2 = patches.Rectangle((-1.5,1.5),3,1.5,fill=False,lw=2,color='b') #unten
r3 = patches.Rectangle((-1.5,6),1.0,1.5,fill=False,lw=2,color='b') #oben links
r4 = patches.Rectangle(( 0.5,6),1.0,1.5,fill=False,lw=2,color='b') #oben rechts
#r5 = plt.Rectangle((0,0),l,5,fill=False,lw=2,color='b')
#Pfeile
#x, y, dx, dy
ax.arrow(-1.0, 10, 0, -2.5,width=0.02,head_width=0.2,head_length=0.8,length_includes_head=True,color='k') #links oben
ax.arrow(1.0, 11.5, 0, -4.0,width=0.02,head_width=0.2,head_length=0.8,length_includes_head=True,color='k') #rechts oben
ax.arrow(-1.5, 2.2, -1.5, 0,width=0.05,head_width=0.3)#unten
ax.arrow(3.3, 6.2, -1.5, -1.5,width=0.025,head_width=0.3)#Namensraum
#y,x, Laenge
ax.hlines(11.5,-3.5,1,lw=2,color='k')
ax.hlines(10,-1,-3.5,lw=1.5,color='k')
#links=1
ax.text(-4,11.2,"11",color='r',fontsize='12')
ax.text(-4,9.7,"42",color='r',fontsize='12')
ax.text(-4.2,1.9,"53",color='r',fontsize='12')
ax.text(-1.1,6.5,"a",color='r',fontsize='12')
ax.text(0.9,6.5,"b",color='r',fontsize='12')
ax.text(-0.25,2,"a + b",color='r',fontsize='12')
ax.text(2.5,6.5,"Namensraum",color='k',fontsize='12')
ax.add_patch(r1)
ax.add_patch(r2) #Ausgabe
ax.add_patch(r3)
ax.add_patch(r4)
ax.axis('off')
fig.tight_layout()
plt.show()
