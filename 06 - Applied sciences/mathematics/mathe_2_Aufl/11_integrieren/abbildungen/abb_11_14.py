#abb_11_14.py
#Integrationsfläche: Dreieck
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,2,500)
y=-2*x+2
#
#fig,ax = plt.subplots(figsize=(8,4))
fig,ax = plt.subplots()
ax.set_xlim(0,1.2)
ax.set_ylim(0,2.5)
ax.plot(x,y,'r-',lw=2)
ax.fill_between(x,y,facecolor='g',alpha=0.2)
ax.text(0.2,0.5,"Integrationsfläche")
ax.set_xlabel('x')
ax.set_ylabel('y',rotation=True)
plt.show()

