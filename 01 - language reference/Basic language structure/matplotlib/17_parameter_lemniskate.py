#17_parameter_lemniskate.py
import numpy as np
import matplotlib.pyplot as plt
t=np.linspace(-np.pi,np.pi,200)
a=1
#Parametergleichungen
x=a*np.sqrt(2)*np.cos(t)/(np.sin(t)**2+1)
y=a*np.sqrt(2)*np.cos(t)*np.sin(t)/(np.sin(t)**2+1)
#Darstellung
fig, ax=plt.subplots()
ax.plot(x,y,linewidth=2)
ax.set(xlabel='x',ylabel='y')
ax.grid(True)
plt.show()