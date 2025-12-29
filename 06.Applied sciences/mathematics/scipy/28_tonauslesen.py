#28_tonauslesen.py
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
abtastrate,daten = wavfile.read("sinus440Hz.wav")
t = np.linspace(0, 1, abtastrate)
fig, ax = plt.subplots()
ax.plot(t,daten)
ax.set_xlim(0,0.01)
ax.set(xlabel="Zeit in Sekunden")
plt.show()


'''
fig.savefig('06_041.png')
fig.savefig('06_041.svg')
'''