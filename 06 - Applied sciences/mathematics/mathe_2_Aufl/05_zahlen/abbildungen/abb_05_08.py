#abb_05_08.py
#Rechtecke
import matplotlib.pyplot as plt
from matplotlib import patches
#
fig, ax = plt.subplots(figsize=(9,6))
plt.axis([-10,10,-2.5,2.5])

r1 = patches.Rectangle((0,0), 2, 2,fill=False,lw=2)
r2 = patches.Rectangle((4,0), 4, 1,fill=False,lw=2)
r3 = patches.Rectangle((0,-2.5),2.5,1.6,fill=False,lw=2)
r4 = patches.Rectangle((4,-2.5), 2.05, 1.59121,fill=False,lw=2)
ax.add_patch(r1)
ax.add_patch(r2)
ax.add_patch(r3)
ax.add_patch(r4)

ax.text( 8.2,0.35,r"$1,0$",fontsize=12)
ax.text( 5.8,-0.4,r"$2,0$",fontsize=12)

ax.text( 0.9,-2.8,r"$1,5$",fontsize=12)
ax.text( 2.7,-1.8,r"$1,333$",fontsize=12)

ax.text( 4.7,-2.8,r"$1,4167$",fontsize=12)
ax.text( 6.3,-1.8,r"$1,4118$",fontsize=12)

ax.text(0.9,-0.4,r"$a$",fontsize=12)
ax.text(2.1,0.9,r"$a$",fontsize=12)

ax.text( 0.75,0.9,r"$A = 2$",fontsize=12)
ax.text( 5.9,0.4,r"$2$",fontsize=12)
ax.text( 1.2,-1.8,r"$2$",fontsize=12)
ax.text( 4.9,-1.8,r"$2$",fontsize=12)

ax.axis('equal')
ax.axis('off')
#fig.tight_layout()
plt.show()