#L_06_10.py
#Vergleich von exponentiellem und logistischem Wachstum
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
K=100  #Kapazität
r=0.5  #Wachstumsrate    
b=r/K
tmax=24
y0=[1] #Anfangswert
#exponentielles Wachstum
def dgl1(t,y0,r):
    N = y0   
    dN_dt=r*N
    return dN_dt
#logistisches Wachstum
def dgl2(t,y0,r,b):
    N = y0   
    dN_dt=r*N-b*N**2
    return dN_dt

t = np.linspace(0,tmax,500)
z1=solve_ivp(dgl1,[0,tmax],y0,args=(r,),dense_output=True)
z2=solve_ivp(dgl2,[0,tmax],y0,args=(r,b),dense_output=True)
N1 = z1.sol(t).flatten()
N2 = z2.sol(t).flatten()
fig,axes=plt.subplots(2,1,figsize=(6,6))
#exponentielles Wachstum
axes[0].plot(t, N1,"r-",lw=2)
axes[0].set(xlabel="Zeit",ylabel="Anzahl",title="exponentielles Wachstum")
axes[0].grid(True)
#logistisches Wachstum
axes[1].plot(t, N2,"b-",lw=2)
axes[1].set(xlabel="Zeit",ylabel="Anzahl",title="logistisches Wachstum")
axes[1].grid(True)
fig.tight_layout()
plt.show()
