#abb_05_01.py
#Veranschaulich von Zahlenmengen
import matplotlib.pyplot as plt
from matplotlib import patches
#
x1,x2=-32,32
y1,y2=-15,15
#
fig,ax=plt.subplots()
ax.axis([-5,80,-15,15])
#x,y, a, b
k_N=patches.Arc((20, 0),20,10,angle=0,theta1=0,theta2=360,lw=2,edgecolor='black')
k_Z=patches.Arc((24, 0),35,15,angle=0,theta1=0,theta2=360,lw=2,edgecolor='r')
k_Q=patches.Arc((30, 0),50,20,angle=0,theta1=0,theta2=360,lw=2,edgecolor='b')
k_R=patches.Arc((33, 0),65,25,angle=0,theta1=0,theta2=360,lw=2,edgecolor='g')
k_C=patches.Arc((36, 0),80,30,angle=0,theta1=0,theta2=360,lw=2,edgecolor='black')
#
ax.add_patch(k_N)
ax.add_patch(k_Z)
ax.add_patch(k_Q)
ax.add_patch(k_R)
ax.add_patch(k_C)
#
ax.set_title("Zahlenmengen")
ax.text(18,-0.5,r"$\mathbb{N}$",fontsize=15)
ax.text(34,-0.5,r"$\mathbb{Z}$",fontsize=15)
ax.text(45,-0.5,r"$\mathbb{Q}$",fontsize=15)
ax.text(58,-0.5,r"$\mathbb{R}$",fontsize=15)
ax.text(69,-0.5,r"$\mathbb{C}$",fontsize=15)
#ax.set_aspect('equal')
ax.set_xticks([])
ax.set_yticks([])
ax.set_ylim(y1-2,y2+2)
ax.axis('off')
plt.show()



