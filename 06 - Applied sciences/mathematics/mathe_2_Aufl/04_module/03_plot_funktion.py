#03_plot_funktion.py
import numpy as np
import matplotlib.pyplot as plt
#x-Werte
x = np.linspace(0, 10, 500)
#mathematische Funktionen definieren
y1 = x**2
y2=-10*x+100
#Grafikbereich
fig, ax = plt.subplots(figsize=(6,6))
ax.set_title("Funktionsplot")
ax.set_xlabel('x')
ax.set_ylabel('y',rotation=True)
ax.plot(x,y1,'r--',lw=2,label='$y_1=x^{2}$')
ax.plot(x,y2,'b-',lw=2,label='$y_2=-10\cdot x+100$')
ax.plot(6.18,38.2,'ro')
ax.legend(loc='best')
ax.text(6.5,37,"Schnittpunkt")
ax.set_xticks(np.arange(0, 11, 1))
ax.set_yticks(np.arange(0, 110, 10))
ax.grid(True)
#fig.savefig('parabel.png')
plt.show()

'''
ax.set(xlabel='x',ylabel='y',title='Funktionsplot')
ax.axis([0,10,0,100])
'''

# fig.savefig("/Users/veit/documents/Python_Mathe/Export_Mathe_Python_neu/Abbildungen/04_003.pdf")
# fig.savefig("/Users/veit/documents/Python_Mathe/Export_Mathe_Python_neu/Abbildungen/04_003.svg")
