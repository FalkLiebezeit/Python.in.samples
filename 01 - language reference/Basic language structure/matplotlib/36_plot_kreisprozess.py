#36_plot_kreisprozess.py
import numpy as np
import matplotlib.pyplot as plt
Tw, Tk= 800, 400 #K
V1,V2=0.2,1 #dm^3
#Funktionsdefinition p=f(V)
def p(V,T):
    R=8.314   #J/(mol*K)
    n=0.045   #mol
    return 1e-2*n*R*T/V
#Grafik-Bereich
fig, ax=plt.subplots()
V=np.linspace(V1,V2,100)
ax.plot(V,p(V,Tw),'r-') #warm
ax.plot(V,p(V,Tk),'b-') #kalt
#Punkte
ax.plot([V1,V1],[p(V1,Tw),p(V1,Tk)],'ko')
ax.plot([V2,V2],[p(V2,Tw),p(V2,Tk)],'ko')
#vertikale Linien
ax.plot([V1,V1],[p(V1,Tk),p(V1,Tw)],'k-')
ax.plot([V2,V2],[p(V2,Tk),p(V2,Tw)],'k-')
ax.set_xlim(0.1,1.2)
ax.set_ylim(0,16)
#x,y Beschriftung
ax.text(V1-0.04,p(V1,Tw)-0.25,'1')
ax.text(V2+0.02,p(V2,Tw),'2')
ax.text(V2+0.02,p(V2,Tk)-0.25,'3')
ax.text(V1-0.04,p(V1,Tk)-0.25,'4')
ax.text(0.6,5.6,r'$Q_{zu}$')
ax.text(0.5,1.8,r'$Q_{ab}$')
ax.text(0.55,3.8,'∆W')
ax.set(xlabel='V in Liter',ylabel='p in bar')
ax.fill_between(V,p(V,Tw),p(V,Tk),alpha=0.2,color='green')
plt.show()