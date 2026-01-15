#abb_05_07.py
#Diagonale eines Quadrates
#Berechnung von √2
from math import sqrt
import matplotlib.pyplot as plt
from matplotlib import patches,lines
#
fig, ax = plt.subplots()
#xmin,xmax,ymin,ymax
ax.axis([-0.5,15.5,-0.1,10.5])
a=10 #Seitenlänge
#xData, yData
al=lines.Line2D([0, 0],[0, a],color='black') #links senkrecht
ar=lines.Line2D([a, a],[0, a],color='black') #rechts senkrecht
ao=lines.Line2D([0, a],[a, a],color='black') #oben waagerecht
au=lines.Line2D([0,sqrt(2)*a],[0, 0],color='black')#unten waagerecht
# q=patches.Rectangle((0,0),a,a,fill=False,lw=2) #Alternative
# ax.add_patch(q)
c=lines.Line2D([0, a],[0, a],color='black')  #Diagonale
d=2*sqrt(2)*a
#Kreisbogen 45°
kreis=patches.Arc((0, 0),d,d,angle=0,theta1=0,theta2=45,edgecolor='red',lw=1,)
#
ax.add_patch(kreis)
ax.add_line(al)
ax.add_line(ar)
ax.add_line(ao)
ax.add_line(au)
ax.add_line(c)
#Beschriftungen
ax.text(  5,-0.9,r"$1$",fontsize=15)
ax.text( 10.3, 4,r"$1$",fontsize=15)
ax.text(13.6,-0.9,r"$\sqrt{2}$",fontsize=15)
ax.text(4,5.5,r"$\sqrt{2} $",fontsize=15)
ax.set_aspect('equal')
ax.axis('off')
plt.show()


