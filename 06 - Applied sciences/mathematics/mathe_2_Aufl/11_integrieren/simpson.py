#simpson.py
'''
Berechnet ein bestimmtes Integral mit der Simpson-Formel.
'''
#Simpson-Regel
def simpson(f,a,b,n=10):
    h=(b-a)/n
    summe=0
    for i in range(0,n):
        summe = summe + f(a+i*h) + 4*f(a+h/2+i*h) + f(a+(i+1)*h)
    return h*summe/6