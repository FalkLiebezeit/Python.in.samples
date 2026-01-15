#abb_01_07.py
#Zahlendarstellung im Computer
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(8,1.2))
#x1,x2,y1,y2
ax.axis([-1,18,-0.1,1.2])
r1 = plt.Rectangle((0,0), 17, 1,fill=False,lw=2,color='b')
#Ursprung x,y,dx,dy,breite
ax.vlines(1.2,0,1,color='r',lw=2)
ax.vlines(7,0,1,color='r',lw=2)
H=0.35
ax.text(0.4,H,"V",fontsize='14')
ax.text(2.2,H,"11 Bit Exponent",fontsize='14')
ax.text(10,H,"52 Bit Mantisse",fontsize='14')
ax.add_patch(r1)
ax.axis('off')
fig.tight_layout()
#fig.savefig("/Users/veit/documents/Python_Mathe/Dateien_fuer_Autor/Abbildungen/01_007.png")
plt.show()
'''
fig.savefig("/Users/veit/documents/Python_Mathe/Dateien_fuer_Autor/Abbildungen/01_007.png")
'''