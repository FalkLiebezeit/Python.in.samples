#abb_05_05.py
#RSA-Sender-Empfänger
import matplotlib.pyplot as plt
from matplotlib import patches
fig, ax = plt.subplots(figsize=(10,5))
#x1,x2,y1,y2
ax.axis([-11,11,-5,5])
r1 = patches.Rectangle((-10,-2.5), 4, 3,fill=False,lw=2)
r2 = patches.Rectangle((6,-2.5), 4, 3,fill=False,lw=2)
#Ursprung x,y,dx,dy,breite
kanal=ax.arrow(-6,-1,10.8,0,fill=False,width=0.85,head_length=1.2,head_width=1.5,color='b')
angreifer=ax.arrow(0,3,0,-2.39,fill=True,width=0.55,head_length=1.2,head_width=1.25,color='r')

ax.add_patch(r1)
ax.add_patch(r2)
ax.add_patch(kanal)
ax.add_patch(angreifer)


ax.text( -1.1,-1.12,"Geheimtext c",fontsize=12)

ax.text(-9.1,-1.12,"Sender A",fontsize=12)
ax.text(6.8,-1.12,"Empfänger B",fontsize=12)
ax.text(-10,-3.5,"öffentlicher Schlüssel e",fontsize=12)
ax.text(-10,-4.3,"öffentlicher Schlüssel n",fontsize=12)

ax.text(6,-3.5,"privater Schlüssel d",fontsize=12,color='r')
ax.text(6,-4.3,"öffentlicher Schlüssel n",fontsize=12)

ax.text( -0.9,3.5,"Angreifer",fontsize=12)

#plt.axis('equal')
ax.axis('off')
fig.tight_layout()
plt.show()
