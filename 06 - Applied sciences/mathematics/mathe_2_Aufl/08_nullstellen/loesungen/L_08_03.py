#L_08_03.py
import numpy as np
import matplotlib.pyplot as plt
#
def f(x):
    return x - np.cos(x),x**2 - np.sin(x), np.exp(x)- x**2/4 - 2,np.log(x+2)-2*x**2
#
fig, ax = plt.subplots(4,figsize=(6,12),label='Nullstellensuche')
x=np.linspace(0,2,200)
#
for i in range(4):
    ax[i].plot(x,f(x)[i])
    ax[i].plot([0,2],[0,0],'k-',lw=0.6)#Nulllinie
#    
fig.tight_layout()
plt.show()

