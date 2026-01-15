#09_001.py
#Tangentensteigung
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,5.0,200,endpoint=True)
x0=1   #Stelle der Steigung
xmax=3
#Parabel
def f(x):
    return x**2
#
def fs(x):
    return m*x + f(2.5)
#
m=2*x0 #Steigung
y0=x0**2 #y-Koordinate für x0

y2_1=m*(x-x0)+y0 #Tangentengleichung
#
fig, ax=plt.subplots(label='Tangentenproblem')
ax.plot(x,f(x),'b-')     #Parabel
#x1, x2, y1,y2
ax.plot([1,2.5],[1,f(2.5)],'r-')    #Sekante
ax.plot(2.5,f(2.5),'ro') #Punkt
ax.plot(x,y2_1,'r--')    #Tangente
ax.plot(x0,y0,'ro') #Punkt
ax.set_title('$y=x^2$')
ax.set_xlim(0,xmax)
ax.set_ylim(-y0,xmax**2)
ax.set_yticks(np.arange(0,xmax**2,1))
#Dreieck
ax.hlines(f(x0),2.5,x0,color='black')
ax.vlines(2.5,f(x0),f(2.5),color='black') #Delta_y
ax.text(1.8,0.5,r'$\Delta x$',fontsize=12) #Delta x
ax.text(2.52,3.1,r'$\Delta y$',fontsize=12) #Delta y
#Steigungswinkel
ax.text(1.5,1.3,r'$\alpha$',fontsize=12) #alpha
ax.text(1.0,1.4,r'$P$',fontsize=12) #P
ax.text(2.4,6.7,r'$Q$',fontsize=12) #Q
ax.text(0.95,-1.95,r'$x_0$') #x0
#
ax.grid(True)
ax.set_ylabel('y',rotation=0)
ax.set_xlabel('x')

plt.show()

