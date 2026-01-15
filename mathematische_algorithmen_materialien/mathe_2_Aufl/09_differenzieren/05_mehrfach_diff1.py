#03_mehrfach_diff1.py
#Funktionsdefinition
def f(x):
    return x**4/32
#Ableitungungen
def diff14(x):
    return x**3/8, 3*x**2/8, 3*x/4, 3/4
#selbstdefinierte Funktion
def diff(f,x,n=1,h=1e-6):
    if n==1:
        h=h
        return (f(x+h)-f(x-h))/(2*h)
    elif n==2:
        h=h*1e3
        return (f(x+h)-2*f(x)+f(x-h))/h**2
    elif n==3:
        h=h*1e4
        return (f(x+2*h)-2*f(x+h)+2*f(x-h)-f(x-2*h))/(2*h**3)
    elif n==4:
        h=h*1e5
        return (f(x-2*h)-4*f(x-h)+6*f(x)-4*f(x+h)+f(x+2*h))/h**4
#Hauptprogramm
x0=2
y1,y2,y3,y4=diff14(x0) #genau
print("1. Ableitung:",diff(f,x0,1),"genau:",y1)
print("2. Ableitung:",diff(f,x0,2),"genau:",y2)
print("3. Ableitung:",diff(f,x0,3),"genau:",y3)
print("4. Ableitung:",diff(f,x0,4),"genau:",y4)

'''
#maschinengenauigkeit.py
eps=1.
while (1.0+eps)!=1.0:
    eps=eps/2.0
#optimale Schrittweite
hopt1=(4*eps*abs(f(x0))/abs(y2))**(1/2) #Knorrenschild, S. 115
hopt2=(3*eps*abs(f(x0))/abs(y3))**(1/3) #Knorrenschild, S. 176
hopt4=(48*eps*abs(f(x0))/abs(y4))**(1/4) #Knorrenschild, S. 176
print(eps)
print(hopt1)
print(hopt2)
print(hopt4)
'''


