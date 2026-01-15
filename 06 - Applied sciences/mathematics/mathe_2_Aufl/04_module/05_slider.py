#05_slider.py
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
#Slider-Einstellung abfragen
def update(val):
    x=sldX.val
    txtY.set_text("y=%.2f"%x**2)
#Grafikbereich
fig,ax=plt.subplots(figsize=(6,1.5),label='Slider')
fig.subplots_adjust(left=0.12,bottom=0.5)
txtY=ax.text(0.45,0.5,'y=25') #Text
dicB={'size':'12','facecolor':'red'}
#x1, y1, x2, y2
xySlider = fig.add_axes([0.1, 0.18, 0.8, 0.12])
sldX=Slider(xySlider,'x',valmin=1,valmax=10,valinit=5,handle_style=dicB)
sldX.on_changed(update)
ax.set_xticks([])
ax.set_yticks([])
ax.set_frame_on(False)
plt.show()

# fig.savefig("/Users/veit/documents/Python_Mathe/Export_Mathe_Python_neu/Abbildungen/04_005.pdf")
# fig.savefig("/Users/veit/documents/Python_Mathe/Export_Mathe_Python_neu/Abbildungen/04_005.svg")

# print(type(Slider))



