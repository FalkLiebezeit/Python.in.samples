#abb_11_12.py
#Integrationsfläche Rechteck
import numpy as np
import matplotlib.pyplot as plt
#
x1,x2=0,2
y1,y2=0,1
dx=0.2
dy=0.2
x=np.linspace(0,x2,500)
#
fig,ax = plt.subplots(figsize=(8,4))
ax.set_ylim(0,1.2)
ax.vlines(x1,y1,y2,color='k')
ax.vlines(x2,y1,y2,color='k')
ax.vlines(x1+dx,y1,y2,color='k') #Delta_x
ax.hlines(y2,x1,x2,color='k')
ax.hlines(y2-dy,x1,x1+dx,color='k')
ax.hlines(y2-2*dy,x1,x1+dx,color='k')
ax.hlines(y2-3*dy,x1,x1+dx,color='k')
ax.hlines(y2-4*dy,x1,x1+dx,color='k')
#Fuellen
ax.fill_between(x,y2,facecolor='g',alpha=0.2)
ax.text(0.7,0.5,"Integrationsfläche")
ax.text(0.07,1.04,r"$\Delta x$")
ax.text(0.25,0.86,r"$\Delta y$")
ax.text(0.07,0.86,r"$\Delta A$")
ax.set_xlabel('x')
ax.set_ylabel('y',rotation=True)
plt.show()
