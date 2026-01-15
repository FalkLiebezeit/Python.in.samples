#11_004.py
#Mittelpunktregel
import numpy as np
import matplotlib.pyplot as plt
n=10
#
def f(x):
    return x**2
#
def rechteck():
    #vertikal: x-, ymin, ymax
    ax.vlines(4,0,f(6),color='b')
    ax.vlines(8,0,f(6),color='b')
    ax.vlines(6,0,f(6),color='r',linewidth=0.5)
    #horinzontal: y-, xmin, xmax
    ax.hlines(f(6),4,8,color='b')
#    
fig,ax = plt.subplots()
x=np.linspace(0,10,100)
#Koordinaten
ax.hlines(0.25,0.5,10,color='black',linewidth=1)
ax.vlines(0.0,0,100,color='black',linewidth=1)
#Mittelpunkt
ax.scatter(6,f(6),color='red')
ax.plot(x,f(x),color='black',lw=1.5)
rechteck()
ax.set_xlim(0,11)
ax.set_ylim(0,105)
ax.text(5,12,r'$\frac{h}{2} $',fontsize='14')
ax.text(7,12,r'$\frac{h}{2} $',fontsize='14')
ax.text(3.85,-3.5,r'$x_{i}$',fontsize='12')
ax.text(7.85,-3.5,r'$x_{i+1}$',fontsize='12')
ax.text(-0.75,90,r'$f\left(x\right)$',fontsize='12')
ax.annotate(r'$f\left(\frac{x_{i}+x_{i+1}}{2}\right)$',
             xy=(6,f(6)),
             xytext=(3.5,50),
             fontsize=16,
             arrowprops=dict(width=1,headwidth=5,facecolor='blue')
            )

ax.set_xticks([])
ax.set_yticks([])
ax.axis('off')
#plt.tight_layout()

plt.show()

