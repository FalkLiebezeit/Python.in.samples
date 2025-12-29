#L_09_04.py
import numpy as np
N=50 #Grundgesamtheit
sollwert=100
a=100.2  #untere Grenze
b=100.5  #obere Grenze
s=1 #Standardabweichung
#Berechnungen
werte=sollwert + s*np.random.normal(size=N)
werte=np.round(werte,2)
swerte=np.sort(werte)
count1=count2=0
for i in range(N):
    if a>=swerte[i]:
        count1=count1+1
    else:
        break
for i in range(N):
    if b>=swerte[i]:
        count2=count2+1
    else:
        break
count=count2-count1
h=100*count/N
#Ausgaben
print(swerte)
print("absolute Wahrscheinlichkeit:",count)
print("relative Wahrscheinlichkeit:",h,"%")
