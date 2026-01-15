#abb_07_01.py
#Rechteck zeichnen
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
fig, ax = plt.subplots(figsize=(6,3))
#x1,x2,y1,y2
ax.axis([-1,41,-2,41])

r1 = Rectangle((0,0),20,40,fill=False,lw=2,color='b')

ax.text(9.5,18,r"$n^{2}$",color='r',fontsize='14')
ax.text(21,18,r"$n$",color='r',fontsize='14')
ax.text(9.5,-3.8,r"$n$",color='r',fontsize='14')

ax.add_patch(r1)
ax.axis('off')
plt.show()

