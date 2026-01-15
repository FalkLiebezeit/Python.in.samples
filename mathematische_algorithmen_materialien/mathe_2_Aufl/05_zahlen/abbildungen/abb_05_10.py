#abb_05_10.py
#Achteck
from math import pi,sqrt
import matplotlib.pyplot as plt
import matplotlib as mlt
#
fig, ax = plt.subplots(figsize=(7,7))
plt.axis([-10,10,-10,10])
r=18
w=360
#y, xmin, xmax,
plt.hlines(  9,-9,9,color='black')
plt.hlines(  3,-9,9,color='black')
plt.hlines( -3,-9,9,color='black')
plt.hlines( -9,-9,9,color='black')
#x, ymin, ymax
plt.vlines(-9,-9,9,color='black')
plt.vlines(-3,-9,9,color='black')
plt.vlines( 3,-9,9,color='black')
plt.vlines( 9,-9,9,color='black')
#[x1,x2],[y1,y2]
l1=plt.Line2D([-9,-3], [3, 9],color='black') 
l2=plt.Line2D([3, 9], [9, 3],color='black')
l3=plt.Line2D([-9, -3], [-3, -9],color='black')
l4=plt.Line2D([3, 9], [-9, -3],color='black')
kreis=mlt.patches.Arc((0, 0),r,r,angle=w,edgecolor='r',lw=2)
ax.add_patch(kreis)
ax.add_line(l1)
ax.add_line(l2)
ax.add_line(l3) 
ax.add_line(l4)
ax.set_aspect('equal')
ax.set_xticks([])
ax.set_yticks([])
#plt.box(on=None)
ax.axis('off')
ax.text( -0.8,-0.6,r"$\Delta A=\frac{1}{9}$",fontsize=12)
ax.text( -0.8,-10,r"$d\  =\  1$",fontsize=12)
plt.show()