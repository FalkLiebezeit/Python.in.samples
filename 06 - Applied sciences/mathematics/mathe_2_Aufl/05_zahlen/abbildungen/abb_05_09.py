#abb_05_09.py
#3 Kreise
import matplotlib.pyplot as plt
import matplotlib as mlt
#
fig, ax = plt.subplots(figsize=(8,4))
#x1,x2,y1,y2
ax.axis([-12,12,-6,6])
r1=5
r2=6
r3=8
w=360
kreis1=mlt.patches.Arc((-9, 0),r1,r1,angle=w,edgecolor='r',lw=2,ls='dotted')
kreis2=mlt.patches.Arc((-2, 0),r2,r2,angle=w,edgecolor='g',lw=2,ls='dashed')
kreis3=mlt.patches.Arc((6.5, 0),r3,r3,angle=w,edgecolor='k',lw=2,ls='dashdot')
l1=plt.Line2D([-10,5], [-5,-5],color='r',lw=1) 
l2=plt.Line2D([-10,-5], [-5.5,-5.5],color='b',lw=1)
ax.add_patch(kreis1)
ax.add_patch(kreis2)
ax.add_patch(kreis3)
ax.add_line(l1)
ax.add_line(l2)

ax.set_aspect('equal')
ax.set_xticks([])
ax.set_yticks([])
plt.box(on=None)
ax.text(-9.5,3.5,r"$U_{1}$",fontsize=12)
ax.text(-2.5,4.5,r"$U_{2}$",fontsize=12)
ax.text( 6,5,r"$U_{3}$",fontsize=12)
ax.text(-9.5,0,r"$d_{1}$",fontsize=12)
ax.text(-2.5,0,r"$d_{2}$",fontsize=12)
ax.text(6,0,r"$d_{3}$",fontsize=12)
ax.text( -8,-4.5,r"$U$",fontsize=12)
ax.text( -8,-6.5,r"$d$",fontsize=12)
plt.show()