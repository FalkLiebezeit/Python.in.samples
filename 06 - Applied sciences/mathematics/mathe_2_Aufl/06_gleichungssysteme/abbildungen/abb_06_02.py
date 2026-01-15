#abb_06_02.py
#Koeffizientenmatix
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
fig, ax = plt.subplots(figsize=(6,3))
#x1,x2,y1,y2
ax.axis([-1,45,-1,36])
h=35
r1 = Rectangle((0,0),20,h,fill=False,lw=2,color='b')
r2 = Rectangle((25,0),5,h,fill=False,lw=2,color='b')
r3 = Rectangle((35,0),5,h,fill=False,lw=2,color='b')

ax.text(2.5,16,"Koeffizientenmatrix",color='r',fontsize='14')
ax.text(26.5,8.2,"Lösungsvektor",color='r',fontsize='14',rotation=90)
ax.text(36.5,3.3,"Inhomogenitätsvektor",color='r',fontsize='14',rotation=90)
ax.text(22,15,"*",color='r',fontsize='18')
ax.text(32,15,"=",color='r',fontsize='18')
ax.add_patch(r1)
ax.add_patch(r2)
ax.add_patch(r3)
ax.axis('off')
fig.tight_layout()
plt.show()
