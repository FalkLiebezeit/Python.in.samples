#03_plot_richtungsfeld.py
import numpy as np
import matplotlib.pyplot as plt
a=1  #Anfangswert
b=-2 #Wachstumskonstante
Nx,Ny = 20,20  #Anzahl der Tangenten
x1,x2 = 0,2         
y1,y2 = 0,1      
#Steigungsfunktion
def f(t,y):
    dy_dt = b*y
    return dy_dt
#Gitter des Richtungsfeldes
x12 = np.linspace(x1,x2,Nx)
y12 = np.linspace(y1,y2,Ny)
x,y = np.meshgrid(x12,y12)
#Lösungskurve
t = np.linspace(x1,x2,200)
f_t=a*np.exp(b*t)
#Grafikbereich
fig,ax = plt.subplots()
#Richtungsfeld zeichnen
ax.quiver(x,y,np.ones_like(x),f(x,y),width=0.002,headwidth=0,color='r')
#Lösungskurve zeichnen
ax.plot(t,f_t,'b--',lw=2)
#Beschriftungen
ax.set_title("Richtungsfeld")
ax.set_xlabel("t")
ax.set_ylabel(r"$\dot{y}$",rotation=0)
plt.show()

