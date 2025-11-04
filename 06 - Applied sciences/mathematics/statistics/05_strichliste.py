#05_strichliste.py
import numpy as np

werte=np.loadtxt("./DataInput/daten.txt")

n=len(werte)
k=int(np.sqrt(n)+0.5)
minimum=np.amin(werte)
maximum=np.amax(werte)
R=round(maximum-minimum,2)
w=round(R/k,2)
swerte=np.sort(werte)
H,I=np.histogram(werte, bins=k)
h=100*H/n

print("Messwerte:\n",swerte)
print("Minimaler Wert:", minimum)
print("Maximaler Wert:", maximum)
print("Spannweite:",R)
print("Anzahl der Klassen:", k)
print("Klassenweite:", w)
print("Bereiche:", np.around(I,decimals=2))
print("absolute Häufigkeit:", H)
print("relative Häufigkeit:", h,"%")
print("Anzahl der Messwerte:", sum(H))