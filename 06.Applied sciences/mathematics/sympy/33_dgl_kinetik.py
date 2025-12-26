#33_dgl_kinetik.py
from sympy import symbols,Eq,Function,plot,N
from sympy.solvers.ode.systems import dsolve_system
t = symbols("t")
cA = Function("cA")
cB = Function("cB")
cC = Function("cC")
k1=0.0295     #1/min, U in Np
k2=2.0483e-4  #1/min, Np in Pu
#DGL-System
dgl1=Eq(cA(t).diff(t,1),-k1*cA(t)) #Edukt
dgl2=Eq(cB(t).diff(t,1), k1*cA(t)-k2*cB(t)) #Intermediat
dgl3=Eq(cC(t).diff(t,1), k2*cB(t)) #Produkt
#Anfangswerte
aw={
    cA(0): 1, #mol/dm^3
    cB(0): 0,
    cC(0): 0
    }
#Lösung des DGL-Systems
gleichungen = [dgl1,dgl2,dgl3]
aL=dsolve_system(gleichungen)        #allgemeine Lösung
sL=dsolve_system(gleichungen,ics=aw) #spezielle Lösung
gA=sL[0][0].rhs #Edukt
gB=sL[0][1].rhs #Intermediat
gC=sL[0][2].rhs #Produkt
#Ausgaben
print("allgemeine Lösung\n",aL)
print("spezielle Lösung")
print("cA(t) =",N(gA,3))
print("cB(t) =",N(gB,3))
print("cC(t) =",N(gC,3))
p=plot(gA,gB,gC,(t,0,600),show=False,legend=True)
p.title='Folgereaktion'
p.xlabel='t in min'
p.ylabel='Konzentration'
p[0].line_color='blue'
p[0].label='Uran'
p[1].line_color='green'
p[1].label='Neptunium'
p[2].line_color='red'
p[2].label='Plutonium'
p.show()

'''
p.save('folgereaktion.png')
p.save('folgereaktion.svg')
'''
