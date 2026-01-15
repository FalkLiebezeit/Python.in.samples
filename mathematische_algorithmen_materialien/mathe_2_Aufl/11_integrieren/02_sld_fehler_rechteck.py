#02_sld_fehler_rechteck.py
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
xm=5 #Mittelpunkt
#Parabel
def f(x):
    return x**2
#Stammfunktion
def F(x):
    return x**3/3
#Slider-Einstellungen erfassen
def update(val):
    h = sldH.val  #Schrittweite
    a = xm - h/2. #untere Grenze
    b = xm + h/2. #obere Grenze
    va.set_data([a,a],[0,f(xm)])      #vertikal, links
    vb.set_data([b,b],[0,f(xm)])      #vertikal, rechts
    hab.set_data([a,b],[f(xm),f(xm)]) #horizontal
    Ag=F(b)-F(a)    #Fläche, genau
    Aa=f(a+h/2)*h #f(xm)*h      #Fläche, Rechteck
    Ea=np.abs(Ag-Aa) #Fehler
    txtAg.set_text('A = %2.6f genau' %Ag)
    txtAa.set_text('A = %2.6f approximiert' %Aa)
    txtEa.set_text('E = %1.6f ' %Ea) #Fehler
#Grafikbereich
fig, ax = plt.subplots(label='Bestimmtes Integral',figsize=(6,6))
ax.set_title(r'$A=\int^{b}_{a} x^{2}dx$')
ax.set(xlabel='x',ylabel='y')
ax.set_xlim(0,10)
ax.set_ylim(0,100)
txtAg= ax.text(0.1,95,'A = 50.666667 genau')        #genau
txtAa= ax.text(0.1,90,'A = 50.000000 approximiert') #approximiert
txtEa= ax.text(0.1,85,'E =  0.666667')              #Fehler
x = np.arange(0,10,0.001)
fx, = ax.plot(x,f(x),color='b',lw=1.5) #Parabel
pm, = ax.plot(xm,f(xm),'ro')           #Punkt
va, = ax.plot([xm-1,xm-1],[0,f(xm)],'k-',lw=1)      #links
vm, = ax.plot([xm,xm],[0,f(xm)],'g--',lw=1)          #Mitte
vb, = ax.plot([xm+1,xm+1],[0,f(xm)],'k-',lw=1)      #rechts
hab, = ax.plot([xm-1,xm+1],[f(xm),f(xm)],color='k',lw=1) #horizontal
fig.subplots_adjust(left=0.1,bottom=0.22)
#x-, y-Position, Laenge, Hoehe
xyH = fig.add_axes([0.1, 0.10, 0.8, 0.03])
sldH=Slider(xyH,'h', 0.5, 2,valinit=2,valstep=0.01)
sldH.on_changed(update)
plt.show()

'''
fig.savefig("/Users/veit/documents/Python_Mathe/Export_Mathe_Python_neu/Abbildungen/11_003.pdf")
fig.savefig("/Users/veit/documents/Python_Mathe/Export_Mathe_Python_neu/Abbildungen/11_003.svg")
'''

