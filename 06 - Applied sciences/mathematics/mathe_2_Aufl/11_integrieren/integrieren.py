#integrieren.py
#Rechtecksummen
def rechteck(f,a,b,n=10):
    h=(b-a)/n
    summe=0
    for i in range(0,n):
        summe=summe+f(a+i*h+h/2)
    return h*summe
#Trapez-Regel
def trapez(f,a,b,n=10):
    h=(b-a)/n
    summe=0
    for i in range(1,n):
        summe=summe+f(a+i*h)
    return (summe + (f(a)+f(b))/2)*h
#Simpson-Regel
def simpson(f,a,b,n=10):
    h=(b-a)/n
    summe=0
    for i in range(0,n):
        summe = summe + f(a+i*h) + 4*f(a+h/2+i*h) + f(a+(i+1)*h)
    return h*summe/6
