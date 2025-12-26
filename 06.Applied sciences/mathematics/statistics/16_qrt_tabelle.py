#16_qrt_tabelle.py
import numpy as np
zeilen=5
spalten=10
A3=1.152
B4=1.669
werte = np.loadtxt("./DataInput/daten.txt")
n=len(werte)
tabelle=np.reshape(werte,(zeilen,spalten),order='F')
mw=[]
staw=[]
for i in range(spalten):
    summe1=0
    summe2=0
    for j in range(zeilen):
        summe1=summe1+tabelle[j,i]
        mittelwert=summe1/zeilen
    for j in range(zeilen):    
        summe2=summe2+(mittelwert-tabelle[j,i])**2
        standardabw=np.sqrt(summe2/(zeilen-1))
    mw.append(round(mittelwert,2))
    staw.append(round(standardabw,3))
mmw=np.mean(mw)
mws=np.mean(staw)
OEGm=mmw + A3*mws
UEGm=mmw - A3*mws
OEGs=B4*mws
print("Tabelle der Messwerte:\n",tabelle)
print("Mittelwert der Stichproben:")    
print(mw)
print("Standardabweichung der Stichproben:")
print(staw)
print("Mittelwertkarte")
print("obere Eingriffsgrenze: ",OEGm)
print("untere Eingriffsgrenze:",UEGm)
print("Standardabweichungskarte")
print("obere Eingriffsgrenze:",OEGs)

