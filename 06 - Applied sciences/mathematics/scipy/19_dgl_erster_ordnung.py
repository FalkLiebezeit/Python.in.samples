#19_dgl_erster_ordnung.py
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
U0=10
R,L=1,1
Tau=L/R
tmax=5*Tau
ti=[0,tmax] #Integrationsintervall
IL0 =[0]    #Anfangswert
#DGL 1. Ordnung
def dgl(t,ia):
    i=ia #Anfangswert
    di_dt=(U0-R*i)/L
    return di_dt
#t.shape (500,)
t = np.linspace(0,tmax,500)
#Lösung der DGL
z = solve_ivp(dgl,ti,IL0,dense_output=True)
iL = z.sol(t) #iL.shape (1,500)
#Darstellung der Lösung
fig, ax = plt.subplots()
ax.plot(t, iL.flatten(),"r",lw=2) #iL.flatten().shape (500, )
ax.set(xlabel="t",ylabel="$I_L(t)$")   
ax.grid(True)
#plt.show()
#zum testen
# print(iL.flatten().ndim)
print(z.sol)
# print(iL.shape)
# print(t.shape)
# print(iL.flatten().shape)





