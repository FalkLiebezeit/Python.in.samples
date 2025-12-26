#15_axes_axes.py
import numpy as np
import matplotlib.pyplot as plt
f=50    #Frequenz in Ht
tmax=20 #Zeit in ms
t = np.linspace(0, tmax, 500)
ut=5*np.sin(2*np.pi*f*t*1e-3) + 0.8*np.random.randn(t.size)
fig=plt.figure()
#left, bottom, width, height
ax1=fig.add_axes([0.12,0.1,0.8,0.8]) #außen
ax2=fig.add_axes([0.6,0.6,0.28,0.25])#innen
#x1,x2,y1,y2
ax1.axis([0,tmax,-10,10])
ax2.axis([2.5,3.5,0,10])
#Grafik-Ausgabe
ax1.plot(t,ut,"b-")
ax1.set_xlabel('t in ms')
ax1.set_ylabel('u(t)')
ax2.plot(t,ut,"b-")
plt.show()

'''
#einfache Alternative für Zeile 10
ax1=fig.add_subplot(xlabel='t in ms',ylabel='u(t)',title='Unterdiagramm')
ax1=fig.add_axes([0,0,1,1]) #geht nicht!
print(ax1.get_position()) #Daten für Axes abfragen
'''
# fig.savefig('04_014a.png')
# fig.savefig('04_014a.svg')

