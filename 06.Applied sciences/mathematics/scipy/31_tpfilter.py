#31_tpfilter.py
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal
g=10  #Grad des Filters
f1=10
f2=30
fs=1e3    #Abtastfrequenz
fg=1.1*f1 #Grenzfrequenz
tmax=1
t = np.linspace(0,tmax,2000)
u_t = np.sin(2*np.pi*f1*t) + np.sin(2*np.pi*f2*t)/3
#u_t = 10*np.sin(2*np.pi*f1*t) + 5*np.random.randn(t.size)
TPK = signal.butter(g,fg,'low',analog=False,output='sos',fs=fs)
filtern = signal.sosfilt(TPK, u_t)
fig, ax = plt.subplots(2, 1)
#gemischtes Signal
ax[0].plot(t, u_t)
ax[0].set(ylabel='u(t)',title='10-Hz und 30-Hz Signal')
#gefiltertes Signal
ax[1].plot(t, filtern)
ax[1].set(xlabel='t in s',ylabel='u(t)',title='gefiltertes Signal: 10 Hz')
fig.tight_layout()
plt.show()

'''
fig.savefig('06_044.png')
fig.savefig('06_044.svg')
'''