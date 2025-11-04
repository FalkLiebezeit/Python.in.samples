#23_3d_berg.py
import numpy as np
import matplotlib.pyplot as plt
breite=10
h=100
x=y=np.linspace(-breite,breite,100)
x,y=np.meshgrid(x,y)
#Gleichung für Paraboloid
z=h-x**2-y**2
#Paraboloid darstellen
fig=plt.figure(figsize=(4.2,8))
ax1=fig.add_subplot(2,1,1,projection='3d')
ax1.plot_surface(x,y,z,rstride=5,cstride=5,color='g',edgecolors='y')
ax1.set_zlim(-h,h)
ax1.set(xlabel='x',ylabel='y',zlabel='z',title='Paraboloid')
#Niveaulinien
ax2=fig.add_subplot(2,1,2)
hl=ax2.contour(x,y,z,levels=10,colors='b')
ax2.clabel(hl,inline=True)
ax2.set_xlim(-breite,breite)
ax2.set_ylim(-breite,breite)
ax2.set(xlabel='x',ylabel='y',title='Niveaulinien')
ax2.set_aspect('equal')
plt.show()
'''
Parameter figsize=plt.figaspect(2) in Zeile 11 testen 
#fig.savefig('04_023.png')
'''