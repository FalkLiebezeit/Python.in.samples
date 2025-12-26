#03_interpolation.py
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
ta=np.arange(0,12)
ti=np.arange(0,11,0.01)
#abgetastetes Signal
s=np.sin(ta)
#Interpolationsmethoden
#linear,next,previous,quadratic
f = interp1d(ta, s, kind='cubic')
fig, ax = plt.subplots()
ax.plot(ta,s, 'rx')    #Punkte
ax.plot(ti,f(ti),'b-') #interpoliert
ax.set(xlabel='Zeit', ylabel='Signal')
plt.show()