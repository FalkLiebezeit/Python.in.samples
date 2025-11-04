#27_vektorfeld.py
import numpy as np
import matplotlib.pyplot as plt
n=10
x1,x2=0,10
u=2 #Länge
v=0 #Richtung
xk=yk=np.linspace(x1,x2+u,n)
x,y=np.meshgrid(xk,yk)
fig, ax=plt.subplots()
#Vektoren definieren
ax.quiver(x,y,u,v,units='xy',scale=2,color='blue')
#Bereich der x-Achse
ax.set_xlim(x1-u/2,x2+u)
plt.show()