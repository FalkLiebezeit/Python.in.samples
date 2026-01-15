#abb_09_004.py
#zentraler Differenzenquotient
import numpy as np
import matplotlib.pyplot as plt
sg=11 #Schriftgröße
#Parabel
def f(x):
    return x**2
    #return np.exp(x)
#Tangente
def tangente(x,x0):
    return 2*x0*(x-x0)+f(x0)

x0=3
x1=2
x2=4
delta_x=1
x1=x0-delta_x
x2=x0+delta_x
x=np.linspace(0,5)
fig, ax = plt.subplots(figsize=(10,8))
#Punkte
#Punkt P
ax.plot(x1,f(x1),'ro')
ax.text(1.96,5,'P',fontsize=sg)
#Punkt x0, M
ax.text(2.9,10,'M',fontsize=sg)
ax.plot(x0,f(x0),'ro')
#Punkt Q
ax.plot(x2,f(x2),'ro')
ax.text(3.9,16.9,'Q',fontsize=sg)
#Dreieck
#horizontal
ax.hlines(f(x1),x1,x0,color='black') #links
ax.hlines(f(x0),x0,x2,color='black') #Mitte
ax.text(2.5,2.8,r'$\Delta x$',fontsize=sg)
ax.text(3.4,8.0,r'$\Delta x$',fontsize=sg)
#vertikal
ax.vlines(x2,f(x0),f(x2),color='black') 
ax.text(4.1,11.4,r'$\Delta y$',fontsize=sg)
ax.text(3.1,6.4,r'$\Delta y$',fontsize=sg)
ax.vlines(x0,x2,f(x0),color='black')
ax.vlines(x1,0,f(x1),color='black',linestyle='--',linewidth=0.9)
ax.vlines(x0,0,f(x1),color='black',linestyle='--',linewidth=0.9)
ax.vlines(x2,0,f(x2),color='black',linestyle='--',linewidth=0.9)
#Sekanten
#ax.plot([2,4],[4,16],color='orange')
#x1, x2: y1,y2
ax.plot([x1,x0],[f(x1),f(x0)],color='red') #Sekante1
ax.plot([x0,x2],[f(x0),f(x2)],color='red') #Sekante2
#Tangente
x12=np.linspace(2,4)
ax.plot(x12,tangente(x12,x0),color='g') #Tangente
#Steigungswinkel
ax.text(3.3,9.6,r'$\alpha$',fontsize=sg) #alpha
#Parabel
ax.plot(x,f(x),'b-',lw=1) #Funktion
ax.text(5,25.2,'f(x)',fontsize=sg)
#Achsen
ax.set_xticks([])
ax.set_yticks([])
#Achsen
ax.hlines(0,0,5,color='black')  #x-Achse
ax.vlines(0,0,25,color='black') #y-Achse
#vertikale Linien

#x-Achsen Beschriftung
ax.text(1.8,-1.5,'$x_{0}-\Delta x$',fontsize=sg) #links
ax.text(2.97,-1.5,'$x_0$',fontsize=sg) #Mitte
ax.text(3.8,-1.5,'$x_{0}+\Delta x$',fontsize=sg) #rechts
#y-Achsen Beschriftung
ax.text(-0.6,f(4),r'$f\left( x_{0}+\Delta x\right)$',fontsize=sg)
ax.text(-0.3,f(3),r'$f\left( x_{0}\right)$',fontsize=sg)
ax.text(-0.6,f(2),r'$f\left( x_{0}-\Delta x\right)$',fontsize=sg)
#ax.set_aspect('equal')
ax.axis('off')
plt.show()


