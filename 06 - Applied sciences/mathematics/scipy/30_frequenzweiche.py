#30_frequenzweiche.py
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter,freqs
g=3      #Grad des Filters
fgu=500  #untere Grenzfrequenz in Hz
fgo=5000 #obere Grenzfrequenz in Hz
#Zähler-, Nennerkoeffizienten
bt,at=butter(g,fgu,'lowpass',analog=True)
bb,ab=butter(g,[fgu,fgo],'bandpass',analog=True)
bh,ah=butter(g,fgo,'highpass', analog=True)
#Kreisfrequenz, Frequenzgang
f1, ht_t = freqs(bt,at) 
f2, hb_t = freqs(bb,ab) 
f3, hh_t = freqs(bh,ah)
fig, ax = plt.subplots(figsize=(8,6))
ax.semilogx(f1,20*np.log10(abs(ht_t)))
ax.semilogx(f2,20*np.log10(abs(hb_t)))
ax.semilogx(f3,20*np.log10(abs(hh_t)))
ax.set_title('Frequenzweiche')
ax.set_xlabel('f in Hz')
ax.set_ylabel('Amplitude in dB')
ax.set_xlim(50,20e3)
ax.set_ylim(-20,3)
ax.margins(0, 0.1)
ax.grid(which='both', axis='both')
ax.axvline(fgu, color='red')
ax.axvline(fgo, color='red')
plt.show()