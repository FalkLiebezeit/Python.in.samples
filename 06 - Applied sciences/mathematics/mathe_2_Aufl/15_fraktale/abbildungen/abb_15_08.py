#abb_15_08.py
#Gaußsche Zahlenebene
#Fluchtkreis
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mlt
x=np.linspace(-2,2,100)
#
fig,ax=plt.subplots(figsize=(6,6))
ax.axis([-2.8,2.8,-2.8,2.8])
ax.set_xlim(-2.5,2.5)
ax.set_ylim(-2.5,2.5)
ax.plot( 0,1,'rx')
ax.plot( 1,1,'ro')
ax.plot( -1,1,'ro')
#[x1,x2],[y1,y2]
r=plt.Line2D([0,1],[0,1],color='blue') #Betrag der komplexen Zahl
l_x=plt.Line2D([1,1],[0,1],color='black',ls='--')
l_y=plt.Line2D([0,1],[1,1],color='black',ls='--')
#
winkel=mlt.patches.Arc((0, 0),1.5,1.5,angle=0,theta1=0,theta2=45,edgecolor='r',lw=1,)#Winkel
kreis=mlt.patches.Circle((0, 0),2,fill=False,edgecolor='r',lw=1,ls='--')#Fluchtkreis
#
ax.add_patch(winkel)
ax.add_patch(kreis)
ax.add_line(r)
ax.add_line(l_x)
ax.add_line(l_y)
#x,y1,y2
ax.vlines(0,-2.5,2.5,color='black')
#y,x1,x2
ax.hlines(0,-2.5,2.5,color='black')
#plt.title("Gaußsche Zahlenebene")
ax.text(-0.45,2.2,r"$Im\ c$",fontsize=12)
ax.text(2.03,-0.2,r"$Re\ c$",fontsize=12)
ax.text(0.95,-0.2,r"$1$",fontsize=12)
ax.text(0.33,0.65,r"$\left| c\right| $",fontsize=12) #Betrag von z
ax.text(-0.15,0.95,r"$i$",fontsize=12)
ax.text(0.7,1.2,r"$c=1+i$",fontsize=12)
ax.text(0.5,0.15,r"$\frac{\pi }{4} $",fontsize=12) #Winkel
ax.text(-1.15,1.15,r"$C$",fontsize=12) #Punkt
ax.set_xlabel('reelle Achse')
ax.set_ylabel('imaginäre Achse')
ax.set_aspect('equal')
#plt.grid(True)
plt.show()
