#06_leitung1.py
import numpy as np
P2a=360e6  #Leistung am Leitungsende
U2a=380e3  #Aussenleiterspannung am Leitungsende
l=400      #Leitungslänge
f=50       #Frequenz
phi=0      #Phasenverschiebung 
R=31e-3  #Widerstandsbelag
L=0.8e-3 #Induktivitätsbelag
G=0.02e-6#Ableitungsbelag
C=14.3e-9#Kapazitätsbelag
#Berechnungen
w=2*np.pi*f
U2=U2a/np.sqrt(3)
I2=P2a/(np.sqrt(3)*U2a*np.cos(phi))
Zw=np.sqrt((R+1j*w*L)/(G+1j*w*C))
g=np.sqrt((R+1j*w*L)*(G+1j*w*C))
U1=   np.cosh(g*l)*U2 + Zw*np.sinh(g*l)*I2
I1=np.sinh(g*l)/Zw*U2 +    np.cosh(g*l)*I2
S1=3*U1*np.conjugate(I1)/1e6
eta=1e-4*P2a/np.real(S1)
#Ausgabe
print("Wellenwiderstand: %5.2f\u03A9, %5.1f°" \
      %(np.abs(Zw),np.angle(Zw,deg=True)))
print("Eingangsspannung: %5.2f V, %5.1f°"\
      %(np.abs(U1),np.angle(U1,deg=True)))
print("Eingangsstrom   : %5.2f A, %5.1f°"\
      %(np.abs(I1),np.angle(I1,deg=True)))
print("Eingangsleistung: %5.0f MW %5.0f Mvar"\
      %(np.real(S1),np.imag(S1)))
print("Wirkungsgrad \u03B7 = %5.0f Prozent" %(eta))

