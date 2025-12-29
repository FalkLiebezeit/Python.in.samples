#22_3d_torus.py
import numpy as np
import matplotlib.pyplot as plt
n=100
R=2 #mittlerer Durchmesser
r=1 #Querschnittsdurchmesser
p = np.linspace(0,2*np.pi,n)
t = np.linspace(0,2*np.pi,n)
p,t = np.meshgrid(p,t)
#Parametergleichungen
x=(R+r*np.cos(p))*np.cos(t)
y=(R+r*np.cos(p))*np.sin(t)
z=r*np.sin(p)
#Kreisring zeichnen
ax = plt.figure().add_subplot(projection='3d')
ax.plot_surface(x,y,z,rstride=5,cstride=5,color='y',edgecolors='r')
ax.set(xlabel='x',ylabel='y',zlabel='z',title='Torus')
ax.set_zlim(-3,3)
plt.show()