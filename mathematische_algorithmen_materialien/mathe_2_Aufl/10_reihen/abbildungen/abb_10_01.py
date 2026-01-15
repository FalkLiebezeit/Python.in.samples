#abb_10_01.py
#Quadratzahlen
import matplotlib.pyplot as plt
from matplotlib import patches
#
fig, ax = plt.subplots(figsize=(8,3))
ax.axis([0,15,0,5])
#Quadrate erzeugen
r1 = patches.Rectangle((0,0), 1,1,fill=False,lw=2)
r2 = patches.Rectangle((1,0), 2,2,fill=False,lw=2)
r3 = patches.Rectangle((3,0), 3,3,fill=False,lw=2)
r4 = patches.Rectangle((6,0), 4,4,fill=False,lw=2)
r5 = patches.Rectangle((10,0),5,5,fill=False,lw=2)
#Quadrate einfügen
ax.add_patch(r1)
ax.add_patch(r2)
ax.add_patch(r3)
ax.add_patch(r4)
ax.add_patch(r5)
#Texte einfügen
ax.text(0.4,0.4,"1",fontsize=12)
ax.text(1.8,0.9,"4",fontsize=12)
ax.text(4.3,1.3,"9",fontsize=12)
ax.text(7.6,1.8,"16",fontsize=12)
ax.text(12.1,2.2,"25",fontsize=12)

ax.axis('equal')
ax.axis('off')
#plt.tight_layout()
plt.show()
