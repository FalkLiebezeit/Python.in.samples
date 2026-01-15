#abb_12_06.py
#Fadenpendel
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
#
fig, ax = plt.subplots(figsize=(4.5,4.5))
#x1,x2,y1,y2
ax.axis([-5,100,-1,100])
#x1,y1,x2,y2
decke = mpatches.Rectangle((10,95),40,100,fill=True,lw=2,color='gray')
#x1,x2,y1,y2
ax.plot([10,30],[30,95],color='k',lw=2)
ax.plot([30,30],[50,95],color='k',lw=1,ls='dashed')
# x,y, Radius
farbe='lightblue'
m1 = mpatches.Circle((8,20),10,color=farbe) #Kugel
#Beschriftungen
ax.text(25,51,r"$\varphi$",color='r',fontsize='14') #Winkel
ax.text(64,68,r"$\varphi$",color='r',fontsize='14') #Winkel
ax.text(5.5,19,r"$m$",color='black',fontsize='14') #Masse
ax.text(11,50,r"$l$",color='black',fontsize='14') #Länge
ax.text(71.5,60,r"$F_{G}$",color='black',fontsize='14')
ax.text(54,32,r"$F_{s}$",color='black',fontsize='14')
ax.text(25,15,r"$F_{s}$",color='black',fontsize='14')
ax.add_patch(decke)
ax.add_patch(m1)
#x,y,dx,dy
ax.arrow(70,90,0,-52.8,head_width=1.8,head_length=2.8,color='red') #Fg
ax.arrow(70,90,-20,-45.2,head_width=1.8,head_length=2.8,color='red') #Fn
ax.arrow(49,42,18.2,-7,head_width=1.8,head_length=2.8,color='red') #Fs oben
ax.arrow(17,15,20,-8,lw=0.8,head_width=1.8,head_length=2.8,color='red')#Fs unten
ax.arrow(25,53,-2,1,lw=0.8,head_width=1.8,head_length=2.8,color='red') #Auslenkwinkel
ax.axis('off')
ax.set_aspect('equal')
fig.tight_layout()
plt.show()


