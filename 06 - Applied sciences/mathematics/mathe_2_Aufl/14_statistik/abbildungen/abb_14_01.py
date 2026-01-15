#abb_14_01.py
#Verpackung Erdnüsse
import matplotlib.pyplot as plt
from matplotlib import patches
#
fig, ax = plt.subplots(figsize=(4,4),linewidth=20)
#x1,x2,y1,y2
ax.axis([-1,21,-1,61])
rahmen = patches.Rectangle((0,0),20,60,fill=True,lw=2,color='lightblue',alpha=0.5)
ax.text(6,50,"Erdnüsse",color='r',fontsize='24')
ax.text(4,42,"geröstet und gesalzen",color='darkblue',fontsize='14')
ax.text(5.4,26,"\u2606 \u2606️ \u2606️ \u2606️ \u2606️",color='g',fontsize='20')
ax.text(8.4,9,"Inhalt",color='r',fontsize='14',va='center',weight='bold')
ax.text(9,2,"50 g",color='r',fontsize='14',style='oblique',va='center')
ax.add_patch(rahmen)
ax.axis('off')
fig.tight_layout()
plt.show()
