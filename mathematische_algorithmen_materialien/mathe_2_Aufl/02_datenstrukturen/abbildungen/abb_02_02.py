#abb_02_02.py
#Datenstrukturen Datentypen
import matplotlib.pyplot as plt
from matplotlib import patches, lines
#
fig, ax = plt.subplots(figsize=(6,3))
#x1,x2,y1,y2
ax.axis([0,88,-20,20])

r1 = patches.Rectangle((6,10),17,8,fill=False,lw=2,color='b')
r2 = patches.Rectangle((50,10),25,8,fill=False,lw=2,color='b')
#unten
r11 = patches.Rectangle((1,-15),6,8,fill=False,lw=2,color='b')
r12 = patches.Rectangle((10,-15),8,8,fill=False,lw=2,color='b')
r13 = patches.Rectangle((21,-15),10,8,fill=False,lw=2,color='b')
#Datenstrukturen
r21 = patches.Rectangle((35,-15),12,8,fill=False,lw=2,color='b')
r22 = patches.Rectangle((50,-15),10,8,fill=False,lw=2,color='b')
r23 = patches.Rectangle((63,-15),10,8,fill=False,lw=2,color='b')
r24 = patches.Rectangle((75,-15),10,8,fill=False,lw=2,color='b')
#y,x, Laenge
#Eingänge
ax.text(7,12.4,r"$Datentypen$",color='r',fontsize='12')
ax.text(52,12.4,r"$Datenstrukturen$",color='r',fontsize='12')
ax.text(2.2,-12,r"$int$",color='r',fontsize='12')
ax.text(11.2,-12,r"$float$",color='r',fontsize='12')
ax.text(22,-12,r"$string$",color='r',fontsize='12')
ax.text(38,-12,r"$tuple$",color='r',fontsize='12')
ax.text(53,-12,r"$set$",color='r',fontsize='12')
ax.text(66,-12,r"$list$",color='r',fontsize='12')
ax.text(78,-12,r"$dict$",color='r',fontsize='12')
#[x1,x2],[y1,y2]
l1=lines.Line2D([14,3.7],[9.5,-7.1],color='black') #1
l2=lines.Line2D([14,14],[9.5,-7.1],color='black') #2
l3=lines.Line2D([14,26],[9.5,-7.1],color='black') #3
l4=lines.Line2D([63,41],[9.5,-7.1],color='black') #4
l5=lines.Line2D([63,55],[9.5,-7.1],color='black') #5
l6=lines.Line2D([63,68],[9.5,-7.1],color='black') #6
l7=lines.Line2D([63,80],[9.5,-7.1],color='black') #6
ax.add_patch(r1)
ax.add_patch(r11)
ax.add_patch(r12)
ax.add_patch(r13)
ax.add_patch(r2)
ax.add_patch(r21)
ax.add_patch(r22)
ax.add_patch(r23)
ax.add_patch(r24)
ax.add_line(l1)
ax.add_line(l2)
ax.add_line(l3)
ax.add_line(l4)
ax.add_line(l5)
ax.add_line(l6)
ax.add_line(l7)
ax.axis('off')
fig.tight_layout()
plt.show()
