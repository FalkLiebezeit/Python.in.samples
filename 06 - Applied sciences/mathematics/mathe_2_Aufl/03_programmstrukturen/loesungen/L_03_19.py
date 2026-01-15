#L_03_19.py
#Laufzeit für Matrizenmultiplikation
import time as t
import random as rnd
import numpy as np
import matplotlib.pyplot as plt
liste=[10,20,40,80,100]
for z in liste:
    n=z
    a=[[rnd.randint(2,9)]*n for i in range(n)]
    b=[[rnd.randint(2,9)]*n for i in range(n)]
    c=[[0]*n for i in range(n)]
    t1=t.time()
    for i in range(n):     #Zeilen
        for j in range(n): #Spalten
            c[i][j]=0
            for k in range(n):
                c[i][j]=c[i][j] + a[i][k]*b[k][j]
    t2=t.time()
    delta_t=(t2-t1)*1e3
#Ausgabe
    print("%3d : %6.3f ms" %(z,delta_t))
    plt.plot(k,delta_t,'rx',ms=8)
#Parabel 3.Grades zeichnen
x=np.arange(0,liste[-1],0.1)
c=delta_t/liste[-1]**3
y=c*x**3
print("Konstante c =",c)
plt.plot(x,y,lw=0.8)
plt.xticks(liste)
plt.xlabel('Anzahl der Eingaben')
plt.ylabel('Laufzeit in ms')
plt.show()

