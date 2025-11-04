#22_liste1.py
import statistics as stat
l1=[52.1,48.7,50.1,49.6,51.8]
l2=[50.5,48.5,49.5,51.5,48.8]
l1.extend(l2) #Methode
sl=sorted(l1) #Funktion
n=len(l1)
minimum=min(l1)
maximum=max(l1)
summe=sum(l1)
mittelwert=summe/n
r=maximum-minimum
z=stat.median(l1)
print("sortierte Liste:\n",sl)
print("Anzahl der Elemente:",n)
print("Minimum: %6.2f Maximum %6.2f" %(minimum,maximum))
print("Summe:",summe)
print("Mittelwert:",mittelwert)
print("Median:",z)
print("Spannweite:",r)
