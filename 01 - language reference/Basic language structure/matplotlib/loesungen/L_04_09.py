#L_04_09.py
'''3D-Darstellung einer Kugel'''
import numpy as np
import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D
n=100
r=2 
theta = np.linspace(0,np.pi,n)
phi = np.linspace(0,2*np.pi,n)
phi,theta = np.meshgrid(theta,phi)
#Parametergleichungen
x=r*np.sin(theta)*np.cos(phi)
y=r*np.sin(theta)*np.sin(phi)
z=r*np.cos(theta)
#Kugel
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot_surface(x,y,z,rstride=5,cstride=5,color='y',edgecolors='r')
ax.set_zlim(-3,3)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title("Kugel")
plt.show()
