#abb_05_11.py
#Faktorisierung
from math import pi,sqrt
import matplotlib.pyplot as plt
import matplotlib.lines as lines
fig, ax = plt.subplots(figsize=(6,3))
#x1,x2 y1,y2
ax.axis([-10,10,0,9])

r=18
w=360

#[x1,x2],[y1,y2]
l1=lines.Line2D([0.5,-3], [7.5, 5],color='black') #oben links
l2=lines.Line2D([1, 4], [7.5, 5],color='black') #oben rechts
l3=lines.Line2D([-3.7, -6.4], [3.6, 1.2],color='black') #3
l4=lines.Line2D([-3.5, -1], [3.5, 1],color='black') #7
l5=lines.Line2D([4.3, 1.3], [3.7, 1],color='black') #2
l6=lines.Line2D([4.5, 7], [3.7, 1],color='black') #5
ax.add_line(l1)
ax.add_line(l2)
ax.add_line(l3) 
ax.add_line(l4)
ax.add_line(l5)
ax.add_line(l6)
#ax.set_aspect('equal')
ax.set_xticks([])
ax.set_yticks([])
ax.axis('off')
#plt.box(on=None)
ax.text(0.2,8,r"$210$",fontsize=12)
ax.text(-4,4,r"$21$",fontsize=12)
ax.text( 4,4,r"$10$",fontsize=12)
ax.text(-7,0,r"$3$",fontsize=12)
ax.text( -1,0,r"$7$",fontsize=12)
ax.text( 1,0,r"$2$",fontsize=12)
ax.text( 7,0,r"$5$",fontsize=12)
plt.show()
