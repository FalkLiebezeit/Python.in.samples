#29_tpfrequenzgang.py
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter,freqs
g=3     #Grad des Filters
fg=1    #Grenzfrequenz in Hz
#Zähler-, Nennerkoeffizienten
b,a=butter(g,fg,'lowpass',analog=True)
#Kreisfrequenz, Frequenzgang
omega,h_t = freqs(b,a)
fig, ax=plt.subplots(figsize=(8,6))
ax.semilogx(omega, 20*np.log10(abs(h_t)))
#ax.plot(omega, 20*np.log10(abs(h_t)))
ax.set_title('Butterworth Tiefpass')
ax.set_xlabel('f in Hz')
ax.set_ylabel('Amplitude in dB')
ax.margins(0, 0.1)
ax.grid(which='both', axis='both')
ax.axvline(fg, color='red') #Grenzfrequenz
plt.show()

'''
print(a)
'''