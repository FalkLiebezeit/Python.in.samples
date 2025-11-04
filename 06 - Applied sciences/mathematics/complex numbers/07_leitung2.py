#07_leitung2.py
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
Z1=Zw*np.tanh(0.5*g*l)
Z2=Zw/np.sinh(g*l)
Z3=Z1
Z4=U2/I2
U10=(Z3+Z4)*I2
I10=U10/Z2
I1=I10+I2
U1=Z1*I1+U10
#Ausgabe
print("Z1= %3.2f \u03A9  %3.2fj \u03A9"\
    %(np.real(Z1),np.imag(Z1)))
print("Z2= %3.2f \u03A9  %3.2fj \u03A9"\
    %(np.real(Z2),np.imag(Z2)))
print("Z3= %3.2f \u03A9  %3.2fj \u03A9"\
    %(np.real(Z3),np.imag(Z3)))
print("Ausgangsstrom %5.3f A" %(I2))
print("Eingangsspannung: %5.2f V, %5.1f°"\
      %(np.abs(U1),np.angle(U1,deg=True)))
print("Eingangsstrom   : %5.2f A, %5.1f°"\
      %(np.abs(I1),np.angle(I1,deg=True)))



