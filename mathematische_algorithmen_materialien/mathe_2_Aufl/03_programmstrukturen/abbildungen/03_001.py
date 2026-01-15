#03_001.py
#Black-Box für Python-Funktion
import matplotlib.pyplot as plt
from matplotlib import patches
#
fig, ax = plt.subplots(figsize=(6,3))
#x1,x2,y1,y2
ax.axis([-1,20,-1,10])
rr = patches.Rectangle((5,0),10,8,fill=False,lw=2,color='b')
l=5
#y,x, Laenge
#Eingänge
ax.hlines(7,2,l,lw=1,color='black') 
ax.hlines(5,2,l,lw=1,color='black')
ax.hlines(3,2,l,lw=1,color='black')
ax.hlines(1,2,l,lw=1,color='black')
ax.text(1,6.8,r"$E_{1}$",color='r',fontsize='12')
ax.text(1,4.8,r"$E_{2}$",color='r',fontsize='12')
ax.text(1,2.8,r"$E_{3}$",color='r',fontsize='12')
ax.text(1,0.8,r"$E_{4}$",color='r',fontsize='12')
#Ausgänge
ax.hlines(6,15,18,lw=1,color='black')
ax.hlines(4,15,18,lw=1,color='black')
ax.hlines(2,15,18,lw=1,color='black')
ax.text(18.2,5.8,r"$A_{1}$",color='r',fontsize='12')
ax.text(18.2,3.8,r"$A_{2}$",color='r',fontsize='12')
ax.text(18.2,1.8,r"$A_{3}$",color='r',fontsize='12')
ax.text(6.5,3.8,r"$Berechnungsvorschrift$",color='g',fontsize='12')
ax.add_patch(rr)
ax.axis('off')
fig.tight_layout()
plt.show()