#abb_10_07.py
#Quadratzahlen
import matplotlib.pyplot as plt
#
fig, ax = plt.subplots(figsize=(8,3))
ax.axis([0,1,0,12])
#Quadrate erzeugen
ax.hlines(0,0,12,color='red',lw=2)
ax.hlines(0,4,8,color='blue',lw=4)
ax.vlines(4,-0.2,0.2,color='black')
ax.vlines(6,-0.2,0.2,color='black')
plt.vlines(8,-0.2,0.2,color='black')
#Texte einfügen
ax.text(1,0.4,"Divergenz",fontsize=12)
ax.text(4.5,0.4,"Konvergenzbereich",fontsize=12)
ax.text(9,0.4,"Divergenz",fontsize=12)
ax.text(3.8,-0.8,"-R",fontsize=12)
ax.text(5.92,-0.8,"0",fontsize=12)
ax.text(7.9,-0.8,"+R",fontsize=12)
ax.axis('equal')
ax.axis('off')
fig.tight_layout()
plt.show()

