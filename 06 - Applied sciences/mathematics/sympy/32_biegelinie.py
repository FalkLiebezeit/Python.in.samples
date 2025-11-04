#32_biegelinie.py
from sympy import *
F,Iy,E,l=symbols('F,Iy,E,l')
x = symbols('x')
w = Function('w')(x)
#Eingaben
b=20   #Breite in mm
h=30   #Höhe in mm
lx=1e3 #Länge in mm
Fz=1e2 #Kraft in N
#Lösung der DGL
dgl=Eq(w.diff(x,2),F/(E*Iy)*(l-x))
aL=dsolve(dgl)        #allgemeine Lösung der DGL
rb={                  #Randbedingungen
    w.subs(x,0):0, 
    w.diff(x,1).subs(x,0):0
    }                 
sL=dsolve(dgl,ics=rb) #spez. Lösung
rL=sL.rhs             #rechte Seite der Gleichung
mL=sL.rhs.subs(x,l)   
wmax=mL.subs(F,Fz).subs(l,lx).subs(E,2.1e5).subs(Iy,b*h**3/12)
wx=rL.subs(F,Fz).subs(l,lx).subs(E,2.1e5).subs(Iy,b*h**3/12)
#Ausgaben
print("Breite b =",b,"mm")
print("Höhe   h =",h,"mm")
print("Länge  l =",lx,"mm")
print("Kraft  F =",Fz,"N")
print("allgemeine Lösung\n",aL)
print("spezielle Lösung\n",sL)
print("rechte Seite der Gleichung\n w(x) =",rL)
print(" w(x) =",wx)
print("maximale Durchbiegung\n w(x=l) =",mL,"=",N(wmax,3),"mm")
p=plot(wx,(x,0,lx),ylabel='w(x)',show=False)
#p.save('biegelinie.png')
#p.save('biegelinie.svg')
p.show()

