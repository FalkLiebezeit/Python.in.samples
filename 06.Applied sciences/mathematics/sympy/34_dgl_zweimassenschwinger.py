#34_dgl_zweimassenschwinger.py
from sympy import symbols,Eq,Function,plot,N
from sympy.solvers.ode.systems import dsolve_system
t = symbols("t")
x1 = Function("x1")(t)
x2 = Function("x2")(t)
m=1000 #kg
c=1e7  #N/m
d=1e3  #kg/s
m1,m2=m,2*m
c1,c2,c3=c,c,c
d1,d2,d3=d,d,d 
#DGL-System
dgl1=Eq(m1*x1.diff(t,2)+d1*x1.diff(t,1)+d2*(x1.diff(t,1)\
        -x2.diff(t,1))+c1*x1+c2*(x1-x2),0) 
dgl2=Eq(m2*x2.diff(t,2)+d2*(x2.diff(t,1)-x1.diff(t,1))\
        +d3*x2.diff(t,1)+c2*(x2-x1)+c3*x2,0)
#Anfangswerte
aw={
    x1.subs(t,0): 0.01, #m
    x2.subs(t,0): 0,
    x1.diff(t,1).subs(t,0):0,
    x2.diff(t,1).subs(t,0):0
    }
#Lösung des DGL-Systems
gleichungen = [dgl1,dgl2]
aL=dsolve_system(gleichungen)        #allgemeine Lösung
sL=dsolve_system(gleichungen,ics=aw) #spezielle Lösung
gX1=sL[0][0].rhs #Auslenkung für m1
gX2=sL[0][1].rhs #Auslenkung für m2
#Ausgaben
print("allgemeine Lösung\n",aL)
print("spezielle Lösung")
print("x1(t) =",N(gX1,3))
print("x2(t) =",N(gX2,3))
p=plot(gX1,gX2,(t,0,0.2),show=False,legend=True)
p.xlabel='t'
p.ylabel='Auslenkung in m'
p[0].line_color='blue'
p[0].label='x1'
p[1].line_color='red'
p[1].label='x2'
p.show()

#Quelle für DGl-System: Vöth, S. 80

'''
p.save('05_019.png')
p.save('05_019.svg')
'''