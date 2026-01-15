#abb_01_05.py
#Rechtecke zeichnen
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(6,3))
#x1,x2,y1,y2
plt.axis([-1,18,-0.1,4.1])
r1 = plt.Rectangle((0,0),17,4,fill=False,lw=2,color='b')
l=10
#Ursprung x,y,dx,dy,breite
ax.vlines(l,1,4,lw=2,color='b')
#y,x, Laenge
ax.hlines(4,0,l,lw=2,color='b')
ax.hlines(3,0,l,lw=2,color='b')
ax.hlines(2,0,l,lw=2,color='b')
ax.hlines(1,0,17,lw=2,color='b')
ax.text(12,2.4,"sympy",color='r',fontsize='14')
ax.text(3,3.4,"scipy",color='r',fontsize='14')
ax.text(3,2.4,"matplotlib",color='r',fontsize='12')
ax.text(3,1.4,"numpy",color='r',fontsize='14')
ax.text(7,0.4,"python",color='r',fontsize='14')
ax.add_patch(r1)
ax.axis('off')
fig.tight_layout()
plt.show()
'''
fig.savefig("/Users/veit/documents/Python_Mathe/Dateien_fuer_Autor/Abbildungen/01_005.png")
'''