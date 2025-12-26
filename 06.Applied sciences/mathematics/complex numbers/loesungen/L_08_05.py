#07_leitung2.py
import numpy as np
U1=10   #Eingangsspannung
I1=10e-3#Eingangsstrom
f=1e3   #Frequenz in kHz
l=1
R=60  #Widerstandsbelag
L=0.6e-3 #Induktivitätsbelag
G=1e-6#Ableitungsbelag
C=50e-9#Kapazitätsbelag
#Berechnungen
w=2*np.pi*f
Zw=np.sqrt((R+1j*w*L)/(G+1j*w*C))
g=np.sqrt((R+1j*w*L)*(G+1j*w*C))
U2=    np.cosh(g*l)*U1 - Zw*np.sinh(g*l)*I1
I2=-np.sinh(g*l)/Zw*U1 +   np.cosh(g*l)*I1
Z2=U2/I2
#Ausgabe
print("Leitungslänge:",l, "km")
print("Wellenwiderstand: %5.2f\u03A9, %5.1f°"\
      %(np.abs(Zw),np.angle(Zw,deg=True)))
print("Lastwiderstand  : %5.2f\u03A9, %5.1f°"\
      %(np.abs(Z2),np.angle(Z2,deg=True)))
print("Ausgangsspannung: %5.2f V, %5.1f°"\
      %(np.abs(U2),np.angle(U2,deg=True)))
print("Ausgangsstrom   : %5.2f A, %5.1f°"\
      %(np.abs(I2),np.angle(I2,deg=True)))




