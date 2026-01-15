#L_11_07.py
#Fläche unter einer Sinus-Kurve in ein flächengeliches Rechteck verwandeln
from math import *
import simpson as sim
#Integrand
def f(x):
    return sin(x)
#Hauptprogramm
a,b=0,pi/2
A=sim.simpson(f,a,b)
hoehe=A/(b-a)
print("Flaecheninhalt:      ",A)
print("Hoehe des Rechtecks: ",hoehe)
print("Breite des Rechtecks:",(b-a))

'''
Mittelwertsatz: Integral von 0 bis pi/2 = hoehe*(b-a)
'''

