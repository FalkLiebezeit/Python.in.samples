#20_laufzeit_messen.py
import time as t
import random as rnd
import numpy as np
import matplotlib.pyplot as plt
liste=[100,200,400,800,1600]
for k in liste:
    n=k
    a=[[rnd.randint(2,9)]*n for i in range(n)]
    b=[[rnd.randint(2,9)]*n for i in range(n)]
    c=[[0]*n for i in range(n)]
    t1=t.time()
    for i in range(n):    #Zeilen
        for j in range(n):#Spalten
            c[i][j]=a[i][j] + b[i][j]
    t2=t.time()
    delta_t=(t2-t1)*1e3 #ms
#Ausgabe
    print("%4d : %5.3f ms" %(k,delta_t))
    plt.plot(k,delta_t,'rx',markersize=8)
#Parabel zeichnen
x=np.arange(0,liste[-1],0.1)
c=delta_t/liste[-1]**2
y=c*x**2
print("Konstante c =",c)
plt.plot(x,y,lw=0.8)
plt.xticks(liste)
plt.xlabel('Anzahl der Eingaben')
plt.ylabel('Laufzeit in ms')
#plt.savefig("/Users/veit/documents/Python_Mathe/Export_Mathe_Python_neu/Abbildungen/03_006.pdf")
#plt.savefig("/Users/veit/documents/Python_Mathe/Export_Mathe_Python_neu/Abbildungen/03_006.svg")
plt.show()

#plt.savefig("/Users/veit/documents/Python_Mathe/Export_Mathe_Python_neu/Abbildungen/03_006.png")

