#abb_14_03.py
#Dichtefunktion der Normalverteilung
import numpy as np
import matplotlib.pyplot as plt

def h(x,sigma,my):
    y=np.exp(-0.5*(x-my)**2/sigma**2)/(sigma*np.sqrt(2*np.pi))
    return y

sigma=1
my=50

x = np.arange(45,55, 0.01);

yw=h(my-sigma,sigma,my) #Wendepunkt

sx1,sy1=my-sigma,yw
sx2,sy2=my+sigma,yw
#
fig, ax = plt.subplots()
ax.plot(x, h(x,sigma,my),lw='2',color='b')
ax.plot(sx1,sy1,"ro")
ax.plot(sx2,sy2,"ro")
ax.vlines(sx1,0,sy1,color='red')
ax.vlines(sx2,0,sy2,color='red')
ax.set_xlim(46,54)
ax.set_ylim(0,0.45)
ax.set_title("Dichtefunktion")
ax.set_xlabel("x")
ax.set_ylabel("h(x)")
ax.text(49.6,0.12,"68,27%",fontsize='12')
plt.show()


