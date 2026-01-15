#01_zufallszahlen.py
import numpy as np
sw=50  #Sollwert
n=1000 #Anzahl der Messungen
s=1    #Standardabweichung
x=np.random.normal(sw,s,size=n)
a=np.around(x,decimals=1)
np.savetxt("daten.txt",a,fmt='%2.1f')
b=np.loadtxt("daten.txt")
print("gespeicherte Messwerte ")
print(a[:n//20])
print("Messwerte auslesen")
print(b[:n//20])