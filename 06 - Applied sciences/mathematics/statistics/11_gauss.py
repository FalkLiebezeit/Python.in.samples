#11_gaus.py
import numpy as np
import matplotlib.pyplot as plt
#Dichtefunktion
def g(x,sigma,my):
    y=np.exp(-0.5*(x-my)**2/sigma**2)/(sigma*np.sqrt(2*np.pi))
    return y

s=1
m=0
x = np.arange(m-3*s, m+3*s, 0.01);
y = g(x,s,m)
fig, ax=plt.subplots()
ax.plot(x, y)
ax.plot(-1, g(-s,s,m),"ro")
ax.plot( 1, g( s,s,m),"ro")
ax.set(xlabel="x",ylabel="g(x)")
plt.show()
