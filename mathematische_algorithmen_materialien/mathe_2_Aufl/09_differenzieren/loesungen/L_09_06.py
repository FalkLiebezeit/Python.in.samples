#L_09_06.py
#Koeffizienten für ein Polynom 4. Grades berechnen
from sympy import *
x,a,b,c,d=symbols('x,a,b,c,d')
x1,x2=-6,6
y1,y2=-10,10
e=1
f=a*x**4+b*x**3+c*x**2+d*x+e
df1=diff(f,x,1)
df2=diff(f,x,2)
df3=diff(f,x,3)
#Gleichungen
g1=f.subs(x,-1/2)
g2=df1.subs(x,1)
g3=df2.subs(x,-2)
g4=df3.subs(x,0)
i=0
L=solve((g1,g2,g3,g4),a,b,c,d,dict=True)
fx=f.subs({a:L[i][a],b:L[i][b],c:L[i][c],d:L[i][d]})
#Ausgabe
print("Lösungsmenge:\n",L)
print("a=",L[i][a])
print("b=",L[i][b])
print("c=",L[i][c])
print("d=",L[i][d])
print("f(x)=",fx)
#Darstellung
p=plot(fx,(x,x1,x2),show=False,visible=False,ylim=(y1,y2))
p.show()



