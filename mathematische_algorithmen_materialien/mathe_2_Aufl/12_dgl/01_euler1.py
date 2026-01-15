#01_euler1.py
def f(t,a):
    dy_dt=a*t
    return dy_dt
#Lösung der DGL
a=1
t0,y0=0,10  #Anfangswerte
h=0.2       #Schrittweite
n=10        #Anzahl der Rechenschritte
y=y0
print("Anzahl der Schritte n =",n)
print("Schrittweite        h =",h)
print("Euler \t genau \tFehler")
for i in range(n):
    t = t0 + i*h
    y = y + f(t,a)*h #Euler-Verfahren
    yg=a*t**2/2 + y0 #genau
    print("%2.4f %2.4f %2.4f" %(y,yg,y-yg))

