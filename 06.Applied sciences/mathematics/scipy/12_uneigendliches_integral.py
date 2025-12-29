#12_uneigendliches_integral.py
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integral
U0=10
R=1 #Ohm
C=1 #Farad
tau=R*C #Sekunden
#Spannugsverlauf am Kondensator
def u(t):
    return U0*(1-np.exp(-t/tau))
#Kondensatorstrom
def i(t):
    return U0*np.exp(-t/tau)/R
#Leistung
def p(t):
    return u(t)*i(t)
#obere Grenze->unendlich
g=np.inf
t = np.linspace(0,5,1000)
W=integral.quad(p,0,g)[0]
print("gespeicherte el. Energie:",W,"Ws")
fig, ax = plt.subplots()
ax.plot(t,u(t),"b-",lw=2,label="Spannung")
ax.plot(t,i(t),"r-",lw=2,label="Strom")
ax.plot(t,p(t),"k-",lw=1,label="Leistung")
ax.fill_between(t,p(t),where=p(t)>=0,color='g',alpha=0.2)
ax.legend(loc="best")
ax.annotate(r"$W_{el}$",xy=(2,1),xytext=(1,10))
ax.set(xlabel="Zeit",ylabel="i, u, p")
plt.show()