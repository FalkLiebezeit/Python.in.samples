#abb_07_07.py
#Grenzwert auf den Zahlenstrahl
import numpy as np
import matplotlib.pyplot as plt
N=6
#ax=plt.axes([0,-1,10,1])
def a1(n):
    return 5*(1-1/(n+1))#*(-1)**n

def a2(n):
    return 5*(1+1/(n+1))

n=np.linspace(1,N,N)
y=0+0*n
g=0.65
fig, ax = plt.subplots(figsize=(6,2))
ax.scatter(a1(n)+g,y,marker='o',color='b')
ax.scatter(a2(n)-g,y,marker='o',color='b')
#y,x1,x2
ax.hlines(0,3,7,color='black')
h=0.1
ax.vlines(4.2,-h,h,color='black')
ax.vlines(5,-h,h,color='black')
ax.vlines(5.8,-h,h,color='black')
ax.text(4.0,-0.4,r"$g-\epsilon$",fontsize=11)
ax.text(4.95,-0.4,r"$g$",fontsize=11)
ax.text(5.6,-0.4,r"$g+\epsilon$",fontsize=11)
ax.set_xticks([])
ax.set_yticks([])
ax.set_ylim(-1,1)
ax.axis('off')
plt.show()