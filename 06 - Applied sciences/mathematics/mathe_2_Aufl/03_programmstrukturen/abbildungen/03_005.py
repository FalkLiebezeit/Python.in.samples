#03_005.py
#Klassendiagramm
import matplotlib.pyplot as plt
from matplotlib import patches
#
fig, ax = plt.subplots(figsize=(6,3))
#x1,x2,y1,y2
ax.axis([-1,6.1,-0.1,5.1])
l=4
r1 = patches.Rectangle((0,0),l,5,fill=False,lw=2,color='b')
#y,x, Laenge
ax.hlines(4,0,l,lw=2,color='b')
ax.hlines(2,0,l,lw=2,color='b')
links=1
ax.text(links+0.5,4.3,"Kreis",color='r',fontsize='16',fontweight='bold')
ax.text(links,3.3,"- pi: float",color='r',fontsize='12')
ax.text(links,2.4,"- radius: float",color='r',fontsize='14')
ax.text(links,1.3,"+ umfang()",color='r',fontsize='14')
ax.text(links,0.4,"+ flaeche()",color='r',fontsize='14')
ax.add_patch(r1)
ax.axis('off')
fig.tight_layout()
plt.show()
