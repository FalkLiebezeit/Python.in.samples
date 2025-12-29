#L_04_13.py
'''Simulation einer Fourier-Synthese fuer eine Recheckschwingung'''
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
N=50 #maximale Anzahl der Oberschwingungen
xmax=4*np.pi
#Fourier-Synthese
def fourier(x,n):
    s=0 #fuer Aufsummierung der Oberschwingungen
    for k in range(1,n,2): #k muss eine ungerade Zahl sein
        y=10*np.sin(k*x)/k #Berechnungsvorschrift fuer Fourier-Reihe
        s=s+y #Summe aus den Oberschwingungen bilden
    return s
#Grafikbereich
fig, ax = plt.subplots(figsize=(8,8))#800x800 Pixel
#Zeichenbereich festlegen: Werte müssen zwischen 0 und 1 liegen
fig.subplots_adjust(left=0.13,bottom=0.2)
x=np.linspace(0,xmax,500) #x ist ein Winkel
ax.axis([0,xmax,-12,12])  #Wertebereich für Achsen festlegen
ax.set(xlabel='x',ylabel='Amplitude',title='Fourier-Synthese')
#x-, y-Position, Laenge, Hoehe des Sliders
xyN  = fig.add_axes([0.1, 0.05,  0.8, 0.03])
#Slider-Objekt sldN erzeugen
sldN =Slider(xyN,'n',2,N,valinit=5,valstep=1) #Anzahl der Oberschwingungen einstellen
#Initialisierung des Funktionsplots mit mit Anfangswerten
y, = ax.plot(x,fourier(x,sldN.val),'b-',lw=1) 
#Aenderungen des Sliders abfragen
def update(val):
    n=sldN.val 
    y.set_data(x,[fourier(x,n)]) #ab Version 3.7: Umwandlung in eine Sequenz (Liste!) 
#Aenderungen durchfuehren
sldN.on_changed(update)
plt.show()# alles Anzeigen




