#01_sld_integral_a_b.py
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
#Parabel
def f(x):
    return x**2
#Stammfunktion
def F(x):
    return x**3/3
#Slider-Einstellungen erfassen
def update(val):
    a,b = sldA.val,sldB.val
    fx.set_data(x,f(x))
    pa.set_data([a],[f(a)])
    pb.set_data([b],[f(b)])
    va.set_data([a,a],[0,f(a)])#Linie
    vb.set_data([b,b],[0,f(b)])#Linie
    A=F(b)-F(a)
    txtA.set_text(f'A = {A:2.3f}')
#Grafikbereich
fig, ax = plt.subplots(figsize=(6,6))
ax.set_title(r'$A=\int^{b}_{a} x^{2}dx$')
ax.set(xlabel='x',ylabel='y')
ax.set_ylim(0,100)
fig.subplots_adjust(left=0.1,bottom=0.22)
x = np.arange(0,10,0.01)
fx, = ax.plot(x,f(x),color='b',lw=2)
pa,pb = ax.plot(4,f(4),'ro',6,f(6),'ro')    #Grenzpunkte
va,vb = ax.plot([4,4],[0,f(4)],[6,6],[0,f(6)],color='k',lw=1)
txtA=ax.text(0.1,90,'A=50.667') #Text
#x-, y-Position, Laenge, Hoehe
xyA = fig.add_axes([0.1, 0.10, 0.8, 0.03])
xyB = fig.add_axes([0.1, 0.05, 0.8, 0.03])
sldA=Slider(xyA,'a', 0, 10,valinit=4,valstep=0.1)
sldB=Slider(xyB,'b', 0,10,valinit= 6,valstep=0.1)
sldA.on_changed(update)
sldB.on_changed(update)
plt.show()


'''
fig.savefig("/Users/veit/documents/Python_Mathe/Export_Mathe_Python_neu/Abbildungen/11_002.pdf")
fig.savefig("/Users/veit/documents/Python_Mathe/Export_Mathe_Python_neu/Abbildungen/11_002.svg")
'''

