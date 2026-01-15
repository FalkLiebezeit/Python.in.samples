#37_sld_p_V_Diagramm.py
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
n=0.045  #mol
R=8.314  #J/(mol*K)
#p=f(V), isotherm, T als Parameter    
def p(V,T):
    return 1e-2*n*R*T/V
#Berechnungen
def update(val):
    Tw, Tk = sldTw.val, sldTk.val #warm, kalt
    V1, V2 = sldV1.val,sldV2.val
    Vx = np.arange(V1,V2,0.001)
    y1.set_data(Vx,p(Vx,Tw)) #Isotherme
    y2.set_data(Vx,p(Vx,Tk))
    punkt1.set_data([V1],[p(V1,Tw)]) #Punkt1
    punkt2.set_data([V2],[p(V2,Tw)]) #Punkt2
    punkt3.set_data([V2],[p(V2,Tk)]) #Punkt3
    punkt4.set_data([V1],[p(V1,Tk)]) #Punkt4
    linie1.set_data([V1,V1],[p(V1,Tk),p(V1,Tw)]) #vertikale Linie
    linie2.set_data([V2,V2],[p(V2,Tk),p(V2,Tw)]) #vertikale Linie
    W=n*R*(Tw-Tk)*np.log(V2/V1)
    eta=1-Tk/Tw
    txtW.set_text('W = %.2f J' %W)
    txtEta.set_text(r'$\eta$ = %.2f' %eta)
#Grafikbereich
fig, ax = plt.subplots(figsize=(6,6))
txtW=ax.text(0.9,15,'')
txtEta=ax.text(0.9,14,'') 
fig.subplots_adjust(left=0.12,bottom=0.25)
ax.set_xlim(0.1,1.2)
ax.set_ylim(0,16)
ax.set(xlabel='V in Liter',ylabel='p in bar',title='p-V-Diagramm')
y1, = ax.plot([],[],'k-',lw=2) #Ordinate
y2, = ax.plot([],[],'k-',lw=2) #Ordinate
linie1,linie2 = ax.plot([],[],'r--',[],[],'r--')
punkt1,punkt2 = ax.plot([],[],'bo',[],[],'ro')
punkt3,punkt4 = ax.plot([],[],'go',[],[],'mo')
#x-, y-Position, Laenge, Hoehe
xyV1 = fig.add_axes([0.1, 0.12, 0.8, 0.03])
xyV2 = fig.add_axes([0.1, 0.08, 0.8, 0.03])
xyTw = fig.add_axes([0.1, 0.04, 0.8, 0.03])
xyTk = fig.add_axes([0.1, 0.0,  0.8, 0.03])
#Slider Objekte erzeugen
sldTw=Slider(xyTw,r'$T_{w}$',501,800,valinit=800,valstep=1)   #warm
sldTk=Slider(xyTk,r'$T_{k}$',400,500, valinit=400,valstep=1)  #kalt
sldV1=Slider(xyV1,r'$V_{1}$',0.2,0.5, valinit=0.2,valstep=0.01)
sldV2=Slider(xyV2,r'$V_{2}$',0.6,1, valinit=1.0,valstep=0.01)
#Änderungen abfragen
sldTw.on_changed(update)
sldTk.on_changed(update)
sldV1.on_changed(update)
sldV2.on_changed(update)
plt.show()


