#06_textbox_funktionsplotter.py
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox
x1,x2=0,5
#Funktionsterm auswerten
def auswerten(funktionsterm):
    y = eval(funktionsterm, {'np': np}, {'x': x})
    kurve.set_ydata(y)
    ax.relim()
    ax.autoscale_view()
    fig.canvas.draw()
#Grafikbereich
fig, ax = plt.subplots(label='Funktionsplotter')
x = np.linspace(x1,x2,200)
kurve, = ax.plot(x,np.zeros_like(x),lw=1.5)
fig.subplots_adjust(bottom=0.23)
#x-, y-Position, Breite, Höhe
xyEingabe = fig.add_axes([0.1, 0.05, 0.8, 0.075])
txtEingabe = TextBox(xyEingabe,'y',textalignment='center')
txtEingabe.on_submit(auswerten)
txtEingabe.set_val('-x**2+5*x-3')
ax.set(xlabel='x',ylabel='y')
ax.grid(True)
plt.show()

'''
#Testfunktionen
2*x-2
x**3
x**0.5
np.exp(x)
np.cos(x)
(x-4)*(x-2)*(x-1)
x**3 - 7*x**2 + 14*x - 8
'''

# fig.savefig("/Users/veit/documents/Python_Mathe/Export_Mathe_Python_neu/Abbildungen/04_006.pdf")
# fig.savefig("/Users/veit/documents/Python_Mathe/Export_Mathe_Python_neu/Abbildungen/04_006.svg")
