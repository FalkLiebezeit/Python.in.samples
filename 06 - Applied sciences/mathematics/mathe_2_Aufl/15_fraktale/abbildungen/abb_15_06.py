#abb_15_06.py
#Pythagorasbaum
import matplotlib.pyplot as plt
#
fig,ax=plt.subplots(1,2,figsize=(6,4))
#fig,ax=plt.subplots(1,2)
bild = plt.imread('pythagoras.png')
#Bild links
ax[0].imshow(bild)
ax[0].axis('off')
#Bild rechts
c=8   #Grundlinie
h=c/2 #Hoehe
lw=2  #Linienbreite
#x1,y1,x2,y2
ax[1].plot([0,h],[0,h],color='black',lw=lw)
ax[1].plot([h,c],[h,0],color='black',lw=lw)
ax[1].plot([0,c],[0,0],color='black',lw=lw)
ax[1].axis('off')
ax[1].set_aspect('equal')
fig.tight_layout()
ax[1].text(3.6,-0.8,r"$c$",fontsize=12)
ax[1].text(1.5,2.2, r"$b$",fontsize=12)
ax[1].text(6.2,2.2, r"$a$",fontsize=12)
ax[1].text(1.3,0.45, r"$\alpha$",fontsize=12)
ax[1].text(6.5,0.45, r"$\beta$",fontsize=12)
ax[1].text(3.6,2.9, r"$90°$",fontsize=12)
plt.show()
