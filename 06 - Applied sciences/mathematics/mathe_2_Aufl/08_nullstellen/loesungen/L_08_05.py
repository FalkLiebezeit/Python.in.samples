#L_08_05.py
import numpy as np
import matplotlib.pyplot as plt
#Fixpunktgleichungen
def f(x):
    return np.cos(x),np.sqrt(np.sin(x)),np.log(x**2/4+2),np.sqrt(np.log(x+2)/2)
#Grafikbereich
fig, ax = plt.subplots(4,figsize=(6,12),label='Fixpunktgleichungen')
x=np.linspace(0,2,200)
#
for i in range(4):
    ax[i].plot(x,f(x)[i])
    ax[i].plot(x,x)
#   
fig.tight_layout()
plt.show()
'''
print(f(a)[0],">",a)
print(f(a)[1],">",a)
print(f(a)[2],">",a)
print(f(a)[3],">",a)
#
print(f(b)[0],"<",b)
print(f(b)[1],"<",b)
print(f(b)[2],"<",b)
print(f(b)[3],"<",b)
'''