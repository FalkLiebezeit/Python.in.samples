#L_04_03.py
'''Gasverbrauch'''
import numpy as np
import matplotlib.pyplot as plt
tage=['Mo','Di','Mi','Do','Fr','Sa','So']#Liste
n=len(tage)#Anzahl der Elemente der Liste ermitteln
x=np.arange(1,n,1) #Wertebereich für Tage 
verbrauch=[4,7,5,6,8,4,9] #Verbrauch al Liste anlegen
mw=np.mean(verbrauch)#Mittelwert berechnen
summe=np.sum(verbrauch) #Summe für Verbrauch berechnen
fig,ax = plt.subplots() #ein Figure- und ein Axes-Objekt erzeugen
ax.plot(verbrauch,'ro') #rote Punkte zeichnen
ax.plot(verbrauch,'b-',label='Verbrauch')#einen blauen Linienzug zeichnen
ax.plot([0,n],[mw,mw],'r-.',label='Mittelwert')#eine horizontale Linie zeichnen
ax.set(ylabel='Verbrauch in $m^{3}$',title='Gasverbrauch')
ax.set_xticks(np.arange(n),tage)#x-Achse beschriften
ax.legend(loc='best') #Legende platzieren
txtS=ax.text(-0.2,8,'summe')#text-Objekt für Summe erzeugen
txtM=ax.text(-0.2,7.7,'mw')#text-Objekt Mittelwert erzeugen
txtS.set_text(f'Verbraucht={summe:3.2f} $m^{3}$')#Ergebniss für Verbrauch anzeigen
txtM.set_text(f'Mittelwert={mw:3.2f} $m^{3}$')#Ergebniss für Mittelwert anzeigen
plt.show()