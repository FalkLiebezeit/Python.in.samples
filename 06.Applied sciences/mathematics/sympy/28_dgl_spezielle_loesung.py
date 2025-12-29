#28_dgl_spezielle_loesung.py
from sympy import *
t=symbols("t")
uc=Function("uc")
U1=10
R=2
L=1/2
C=1/4
Us=U1/(L*C)      #Störfunktion
w0=sqrt(1/(L*C)) #Kreisfrequenz
D=R/(2*L*w0)     #Dämpfung
dgl=Eq(uc(t).diff(t,2)+2*D*w0*uc(t).diff(t,1)+w0**2*uc(t),Us)
#Anfangswerte
aw={uc(0):0, uc(t).diff(t,1).subs(t,0):0}
ua_t=dsolve(dgl,uc(t))       #allgemeine Lösung
us_t=dsolve(dgl,uc(t),ics=aw)#spez. Lösung
uc_t=us_t.rhs
#plot(uc_t,(t,0,5))
#Ausgabe
print("allgemeine Lösung\n",ua_t)
print("spezielle Lösung\n",us_t)
print("rechte Seite der Funktion\n uc(t) =",uc_t)
