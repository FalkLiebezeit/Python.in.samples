#L_05_11.py
#Sechsecke, Archimedes
from math import pi,sqrt
import matplotlib.pyplot as plt
#import matplotlib as mlt
import matplotlib.lines as lines
from matplotlib.patches import RegularPolygon,Circle
#
fig, ax = plt.subplots(figsize=(7,7))
ax.axis([-2.1,2.1,-2.1,2.1])
n=6
ra=2
ri=0.866*ra
xy=0,0
w=180
phi1=0 
phi2=pi/n
#[x1,x2],[y1,y2]
l1=lines.Line2D([0, -0.866], [0, 1.5],color='black') #Innenradius
l2=lines.Line2D([0, 0.866], [0, 1.5],color='black')
l3=lines.Line2D([0, 1.732], [0, 1],color='black')   #Außenradius
l4=lines.Line2D([0, 1.732], [0, -1],color='black')
#fig.add_artist(lines.Line2D([0, 1], [1, 0]))
poly1 = RegularPolygon(xy, n, radius=ra,fill=False,orientation=phi1,lw=1)
poly2 = RegularPolygon(xy, n, radius=ri,fill=False,orientation=phi2,lw=1)
kreis=Circle((0,0),ri,fill=False,lw=2,edgecolor='red')
ax.add_patch(poly1)
ax.add_patch(poly2)
ax.add_patch(kreis)
ax.add_line(l1)
ax.add_line(l2)
ax.add_line(l3) #Außenradius
ax.add_line(l4) #Außenradius
ax.set_aspect('equal')
ax.set_xticks([])
ax.set_yticks([])
#plt.box(on=None)
ax.axis('off')
ax.text(-0.4,0.8,r"$r_{i} = 1$",fontsize=12)
ax.text( 0.62,-0.55,r"$r_{a}$",fontsize=12)
ax.text(-0.2,1.55,r"$s_{1}=1$",fontsize=12)
ax.text( 1.8,0,r"$t_{1}=\frac{2}{\sqrt{3} } $",fontsize=12)
plt.show()
