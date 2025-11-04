#27_tonerzeugen.py
import numpy as np
from scipy.io import wavfile
abtastrate = 44100
f=440 #Frequenz in Hz
t = np.linspace(0,1,abtastrate)
amp = np.iinfo(np.int16).max
ton = amp*np.sin(2*np.pi*f*t)
print("Amplitude:",amp)
wavfile.write("sinus440Hz.wav", abtastrate, ton)

