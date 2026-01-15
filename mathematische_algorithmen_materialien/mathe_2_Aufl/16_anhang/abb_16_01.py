#abb_05_11.py
#Thaleskreis
from math import pi,sqrt
import matplotlib.pyplot as plt
import matplotlib as mlt
fig, ax = plt.subplots(figsize=(6,3))
plt.axis([-1,11,-1,5.5])
c=10.
r=c/2
w=360
#[x1,x2],[y1,y2]
a=plt.Line2D([10,7], [0, 4.57],color='black') 
b=plt.Line2D([0, 7], [0, 4.57],color='black')
c=plt.Line2D([0, 10], [0, 0],color='black')
h=plt.Line2D([7, 7], [0, 4.57],color='blue')
kreis=mlt.patches.Arc((r, 0),10,10,-180,180,edgecolor='r',lw=2)
ax.add_patch(kreis)
ax.add_line(a)
ax.add_line(b)
ax.add_line(c) 
ax.add_line(h)
ax.set_aspect('equal')
ax.set_xticks([])
ax.set_yticks([])
plt.tight_layout()
plt.box(on=None)
plt.text( 3.8,3,r"$b$",fontsize=12)
plt.text( 8.5,2.7,r"$a$",fontsize=12)
plt.text( 6,-0.4,r"$c$",fontsize=12)
plt.text( 6.5,2,r"$h$",fontsize=12)
plt.text( 4,0.3,r"$q$",fontsize=12)
plt.text( 8,0.3,r"$p$",fontsize=12)
plt.text( 1,0.2,r"$\alpha$",fontsize=12)
plt.text( 9.2,0.2,r"$\beta$",fontsize=12)
plt.show()
