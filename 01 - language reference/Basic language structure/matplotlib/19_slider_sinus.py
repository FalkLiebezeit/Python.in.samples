#18_slider_sinus.py
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider,Button
fig,ax=plt.subplots()
fig.subplots_adjust(left=0.2,bottom=0.25)
t=np.linspace(0.0,1.0,200)
a0=5
f0=5
s=a0*np.sin(2*np.pi*f0*t)
kurve, = ax.plot(t,s,lw=2,color='blue')
ax.axis([0, 1, -10, 10])
#Objekte für Steuerelemente platzieren
#linker Rand, unterer Rand, Breite, Höhe
xyAmp=fig.add_axes([0.25, 0.15, 0.65, 0.03])
xyFreq=fig.add_axes([0.25, 0.1, 0.65, 0.03])
xyReset=fig.add_axes([0.8,0.025,0.1,0.04])
#Objekte für Steuerelemente erzeugen
sldAmp=Slider(xyAmp,'Amplitude',1,10,valinit=a0,valstep=0.1)
sldFreq=Slider(xyFreq,'Frequenz',1,10,valinit=f0,valstep=0.1)
cmdReset=Button(xyReset,'Reset')

def update(val):
    A = sldAmp.val
    f = sldFreq.val
    kurve.set_data(t,A*np.sin(2*np.pi*f*t))

def reset(event):
    sldFreq.reset()
    sldAmp.reset()
#Ereignisverarbeitung
sldAmp.on_changed(update)
sldFreq.on_changed(update)
cmdReset.on_clicked(reset)
plt.show()
'''
#besser
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider,Button
#Eingaben
a0=5
f0=5
#Funktionsdefinitionen
def s(t): return a0*np.sin(2*np.pi*f0*t)
#Änderungen abfragen
def update(val):
    A = sldAmp.val
    f = sldFreq.val
    kurve.set_data(t,A*np.sin(2*np.pi*f*t))
#Zurücksetzen
def reset(event):
    sldFreq.reset()
    sldAmp.reset()
#Grafikbereich
fig,ax=plt.subplots()
ax.axis([0, 1, -10, 10])
fig.subplots_adjust(left=0.2,bottom=0.25)
t=np.linspace(0.0,1.0,200)
kurve, = ax.plot(t,s(t),lw=2,color='blue')
#Objekte für Steuerelemente platzieren
#linker Rand, unterer Rand, Breite, Höhe
xyAmp=fig.add_axes([0.25, 0.15, 0.65, 0.03])
xyFreq=fig.add_axes([0.25, 0.1, 0.65, 0.03])
xyReset=fig.add_axes([0.8,0.025,0.1,0.04])
#Objekte für Steuerelemente erzeugen
sldAmp=Slider(xyAmp,'Amplitude',1,10,valinit=a0,valstep=0.1)
sldFreq=Slider(xyFreq,'Frequenz',1,10,valinit=f0,valstep=0.1)
cmdReset=Button(xyReset,'Reset')
#Ereignisverarbeitung
sldAmp.on_changed(update)
sldFreq.on_changed(update)
cmdReset.on_clicked(reset)
plt.show()
'''
