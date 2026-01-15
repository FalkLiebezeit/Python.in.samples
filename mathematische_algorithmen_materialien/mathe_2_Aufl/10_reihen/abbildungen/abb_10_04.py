#abb_10_04.py
#konvergierende geometrische Reihe
import matplotlib.pyplot as plt
from matplotlib import patches
#
fig, ax = plt.subplots(figsize=(6,3))
#x1,x2,y1,y2
ax.axis([-5,405,-5,405])
#x1,y1,x2,y2
r1 = patches.Rectangle((0,0),200,400,fill=False,lw=1,color='b') #1
r2 = patches.Rectangle((200,200),200,200,fill=False,lw=1,color='b') #1/2
r3 = patches.Rectangle((200,0),100,200,fill=False,lw=1,color='b') #1/4
r4 = patches.Rectangle((300,100),100,100,fill=False,lw=1,color='b') #1/8
r5 = patches.Rectangle((300,0),50,100,fill=False,lw=1,color='b') #1/16
r6 = patches.Rectangle((350,50),50,50,fill=False,lw=1,color='b') #1/32
r7 = patches.Rectangle((350,0),25,50,fill=False,lw=1,color='b') #1/48
r8 = patches.Rectangle((375,25),25,25,fill=False,lw=1,color='b') #1/48
r9 = patches.Rectangle((375,0),12.5,25,fill=False,lw=1,color='b') #1/48
#y,x, Laenge
ax.text(90,178,r"$1$",color='r',fontsize='12')
ax.text(288,280,r"$1/2$",color='r',fontsize='12')
ax.text(240,77,r"$1/4$",color='r',fontsize='12')
ax.text(332,141,r"$1/8$",color='r',fontsize='12')
ax.text(315,44,r"$1/16$",color='r',fontsize='12')
ax.text(360,62,r"$1/32$",color='r',fontsize='12')
ax.text(353,20,r"$1/64$",color='r',fontsize='8')
#
ax.add_patch(r1)
ax.add_patch(r2)
ax.add_patch(r3)
ax.add_patch(r4)
ax.add_patch(r5)
ax.add_patch(r6)
ax.add_patch(r7)
ax.add_patch(r8)
ax.add_patch(r9)
ax.axis('off')
fig.tight_layout()
plt.show()
