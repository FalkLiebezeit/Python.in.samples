#13_subplot_funktionen.py
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 10, 100)
y1=x
y2=5-x
y3=x**2
y4=1/(0.2*x+1)
fig, ax = plt.subplots(2, 2)
#1. Zeile, 1. Spalte
ax[0,0].set(ylabel='y',title='lineare Funktion')
ax[0,0].plot(x,y1,'b',lw=2)#Blau
ax[0,0].grid(True)
#1. Zeile, 2. Spalte
ax[0,1].set(title='negative Steigung')
ax[0,1].plot(x,y2,'r',lw=2)#rot
ax[0,1].grid(True)
#2. Zeile, 1. Spalte
ax[1,0].set(xlabel='x',ylabel='y',title='Parabel')
ax[1,0].plot(x,y3,'g',lw=2)#gruen
ax[1,0].grid(True)
#2. Zeile, 2. Spalte
ax[1,1].set(xlabel='x',title='Hyperbel')
ax[1,1].plot(x,y4,'k',lw=2)#schwarz
ax[1,1].grid(True)
fig.tight_layout(pad=1.5,w_pad=2)
plt.show()
'''
#zum testen
#in Zeile 9 einfügen
label='mathematische Funktionen'
#zwischen Zeile 3 und 4 einfügen
bf=1.5
bild=(bf*6.4,bf*4.8) #Tupel
#in Zeile 9 als zusätzliches Argument einfügen
figsize=bild
#oder
fig.set_figwidth(6.4) #Standardwert
fig.set_figheight(4.8)#Standardwert
'''

