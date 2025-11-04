#L_06_20.py
#Frequenzgang für Butterworth-Bandsperre 3. Grades
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
fu=50  #untere Grenzfrequenz in Hz
fo=500 #obere Grenzfrequenz in Hz
g=3    #Grad der Bandsperre
b, a = signal.butter(g,[fu,fo],'bandstop',analog=True)
f, h = signal.freqs(b,a)
#Ausgabe
fig,ax = plt.subplots()
ax.semilogx(f,20*np.log10(abs(h)))
ax.set_title('Bandsperre')
ax.set_xlabel('f in Hz')
ax.set_ylabel('Amplitude [dB]')
ax.set_ylim(-20,3)
ax.margins(0, 0.1)
ax.grid(which='both', axis='both')
plt.show()