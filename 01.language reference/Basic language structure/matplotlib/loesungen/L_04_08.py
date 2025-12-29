#L_04_08.py
'''Kreisevolente'''
import numpy as np
import matplotlib.pyplot as plt
a=1
t=np.linspace(0,5*np.pi,200)#Parameter
#Funktionsdefinitionen
x=a*(np.cos(t)+t*np.sin(t))
y=a*(np.sin(t)-t*np.cos(t))
#Darstellungsteil
fig,ax = plt.subplots()
ax.plot(x,y)
plt.show()