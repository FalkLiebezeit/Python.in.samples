#abb_15_14.py
#Fraktale zu Aufgabe
import matplotlib.pyplot as plt
#
fig,ax=plt.subplots(1,3,figsize=(6,2))
#fig,ax=plt.subplots(1,2)
bild1 = plt.imread('baumfraktal.png')
bild2 = plt.imread('hilbert.png')
bild3 = plt.imread('teppich.png')
#Bild links
ax[0].imshow(bild1)
ax[0].axis('off')
ax[0].text(100,960,"Baum-Fraktal",fontsize=11)
ax[1].imshow(bild2)
ax[1].axis('off')
ax[1].text(225,1250,"Hilbert-Kurve",fontsize=11)
ax[2].imshow(bild3)
ax[2].axis('off')
ax[2].text(110,1000,"Sierpinski-Teppich",fontsize=11)
fig.tight_layout()
plt.show()

