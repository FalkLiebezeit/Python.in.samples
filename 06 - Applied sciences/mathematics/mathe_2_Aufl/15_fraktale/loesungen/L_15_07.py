#L_15_06.py
#Baum zeichnen
from turtle import *

def baum(h, n, w=30):
    if n:
        forward(h)
        a = h/1.8 #Astlänge
        left(w)
        baum(a, n-1);
        right(w)
        right(w)
        baum(a,n-1 )
        left(w) 
        backward(h)
    else:
        forward(h)
        backward(h)

h0=200  #Höhe des Stamms
n0=4    #Rekursionstiefe (maximal 15)
phi0=30 #Winkel
penup()
setpos(0,-h0)
pendown()
pensize(2)
left(90)
speed(1)
tracer(False)
baum(h0,n0,phi0)
update()
mainloop()