#13_sympy_dgl.py
from sympy import symbols,Function,diff,dsolve,solve,plot
t = symbols('t')
x = Function('x')
m=1.0   #Masse in kg
d=0.2   #Dämpfung 
c=9.87  #Federkonstante in N/m
#Anfangswerte
aw={
    x(0):5,                     #Auslenkung
    x(t).diff(t,1).subs(t,0):0  #Anfangsgeschwindigkeit
    }
#Lösung der DGL
#dgl=Eq(diff(x(t),t,2) + d/m*diff(x(t),t) + c/m*x(t),0)
#dgl=Eq(x(t).diff(t,2) + d/m*x(t).diff(t) + c/m*x(t),0)
dgl=diff(x(t),t,2) + d/m*diff(x(t),t,1) + c/m*x(t)
aL=dsolve(dgl)        #allgemeine Lösung der DGL
sL=dsolve(dgl,ics=aw) #spezielle Lösung der DGL
x_t = sL.rhs          #rechte Seite der Funktion
#Ausgaben
print("allgemeine Lösung\n",aL)
print("spezielle Lösung\n",sL)
print("rechte Seite der Funktion\nx(t) =",x_t)
plot(x_t,(t,0,5),ylabel='x(t)')

'''
fig.savefig("/Users/veit/documents/Python_Mathe/Export_Mathe_Python_neu/Abbildungen/09_005.pdf")
fig.savefig("/Users/veit/documents/Python_Mathe/Export_Mathe_Python_neu/Abbildungen/09_005.svg")
'''

'''
from sympy import symbols,Function,diff,dsolve,solve,plot
C=solve([aL.rhs.subs(t,0) - 5, diff(aL.rhs,t).subs(t,0) #Konstanten berechnen
sL=aL.rhs.subs(C) #spezielle Lösung
print(type(sL.rhs))
print(type(plot))
plt=plot(x_t,(t,0,5),show=False)
plt.ylabel='x(t)'
print(type(plt))
plt.show()
'''