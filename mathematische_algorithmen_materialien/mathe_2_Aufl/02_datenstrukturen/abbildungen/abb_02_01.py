#abb_02_01.py
#Objekt=Wert, Identität, Typ
import matplotlib.pyplot as plt
from matplotlib import patches, lines
#
fig, ax = plt.subplots(figsize=(6,3))
#x1,x2,y1,y2
ax.axis([0,32,-20,20])
r1 = patches.Rectangle((8,10),12,8,fill=False,lw=2,color='b')
#unten
r11 = patches.Rectangle((1,-15),6,8,fill=False,lw=2,color='b')
r12 = patches.Rectangle((11,-15),6,8,fill=False,lw=2,color='b')
r13 = patches.Rectangle((21,-15),6,8,fill=False,lw=2,color='b')
#y,x, Laenge
ax.text(12,12.4,r"$Objekt$",color='r',fontsize='12')
ax.text(2.5,-12,r"$Wert$",color='r',fontsize='12')
ax.text(12,-12,r"$Identität$",color='r',fontsize='12')
ax.text(23,-12,r"$Typ$",color='r',fontsize='12')
#[x1,x2],[y1,y2]
l1=lines.Line2D([14,3.7],[9.5,-7.1],color='black') #1
l2=lines.Line2D([14,14],[9.5,-7.1],color='black') #2
l3=lines.Line2D([14,24],[9.5,-7.1],color='black') #3

ax.add_patch(r1)
ax.add_patch(r11)
ax.add_patch(r12)
ax.add_patch(r13)

ax.add_line(l1)
ax.add_line(l2)
ax.add_line(l3)

ax.axis('off')
fig.tight_layout()
plt.show()

