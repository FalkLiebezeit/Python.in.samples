#09_plot_raueber_beute.py
import matplotlib.pyplot as plt
y1=500   #Beute
y2=50    #Räuber
c1=0.25  #Reproduktionsrate der Beute
c2=0.5   #Sterberate der Räuber
d1=0.001 #Beutewahrscheinlichkeit
d2=0.001
#DGL
def dgl(t,y1,y2):
    dy1_dt= c1*y1 - d1*y1*y2  #Beute
    dy2_dt=-c2*y2 + d2*y1*y2  #Räuber
    return dy1_dt,dy2_dt
#Lösung der DGL
n=500
t1=0
t2=50
dt=(t2-t1)/n
lt,ly1,ly2=[t1],[y1],[y2]
for i in range(n):
    t=t1+i*dt
    dy1,dy2=dgl(t,y1,y2)
    y1 = y1 + dy1*dt #Beute
    y2 = y2 + dy2*dt #Räuber
    lt.append(t),
    ly1.append(y1)
    ly2.append(y2)
#Grafikbereich
fig,ax = plt.subplots(2,1)
#Räuber-Beute-Beziehung
ax[0].plot(lt,ly1,'b--',label='Beute')
ax[0].plot(lt,ly2,'r',label='Räuber')
ax[0].legend(loc='best')
ax[0].set_xlabel('Zeit')
ax[0].grid(True)
#Phasendiagramm
ax[1].plot(ly1,ly2,'g')
ax[1].set(xlabel='Beute',ylabel='Räuber')
ax[1].grid(True)
fig.tight_layout()
plt.show()
