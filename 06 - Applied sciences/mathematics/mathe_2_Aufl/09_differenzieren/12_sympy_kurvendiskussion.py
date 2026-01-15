#12_sympy_kurvendiskussion.py
from sympy import *
x=symbols('x')
x1,x2=0,5
fx=x**5-15*x**4+85*x**3-225*x**2+274*x-120
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
p=plot(fx,df1,(x,x1,x2),show=False,visible=False,ylim=(-8,4))
p[0].line_color='black'
p[1].line_color='red'
p.show()

'''
p.save("/Users/veit/documents/Python_Mathe/Export_Mathe_Python_neu/Abbildungen/09_009.pdf")
p.save("/Users/veit/documents/Python_Mathe/Export_Mathe_Python_neu/Abbildungen/09_009.svg")
'''
