#L_09_05.py
#Kurvendiskussion
from sympy import *
x=symbols('x')
x1,x2=-4,4
y1,y2=-10,10
fx=0.1*x**6 - 1.4*x**4 + 4.9*x**2 - 3.6
df1=diff(fx,x)
df2=diff(fx,x,2)
x0=solve(fx,x)
m=solve(df1,x,dict=True)
w=solve(df2,x,dict=True)
#Ausgabe
print("Funktionsterm\n",fx)
print("Nullstellen")
print(x0)
print("Extremwerte")
for i in range(len(m)):
    mx=m[i][x].evalf(4)
    if df2.subs(x,mx)<0:
        print("Maxima x=",mx,"y=",fx.subs(x,mx))
    elif df2.subs(x,mx)>0:
        print("Minima x=",mx,"y=",fx.subs(x,mx))
print("Wendepunkte")
for i in range(len(w)):
    wx=w[i][x].evalf(4)
    print(wx,end="|")
#Darstellung
p=plot(fx,df1,(x,x1,x2),show=False,visible=False,ylim=(y1,y2))
p[0].line_color='black'
p[1].line_color='red'
p.show()

