#L_04_04.py
import numpy as np
import matplotlib.pyplot as plt
#x-Werte
x = np.linspace(0, 360, 1000)
#mathematische Funktionen definieren
y1 = 10*np.cos(2*np.pi*x/360.)
y2 = 10*np.sin(2*np.pi*x/360.)
#Grafikbereich
fig, ax = plt.subplots(figsize=(10,5),label='Funktionsplot')
ax.plot(x,y1,'r--',label='$y_1=cos(x)$')
ax.plot(x,y2,'b-', label='$y_2=sin(x)$')
ax.set_title("Sinus- und Cosinus-Funktion")
ax.set_xlabel('x')
ax.set_ylabel('y',rotation=True)
ax.legend(loc='best')
#ax.set_xlim(0,360)
#ax.set_ylim(-11,11)
ax.set_xticks(np.arange(  0, 361, 30))#x-Achse skalieren
ax.set_yticks(np.arange(-10, 11,  2))#x-Achse skalieren
ax.grid(True)
plt.show()
