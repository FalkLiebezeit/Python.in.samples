#L_15_07.py
#Hilbert-Kurve
from turtle import * 
#Winkel, Länge, Rekursionstiefe
def hilbert(w,l,n):
    if n == 0:
        return

    right(w)
    hilbert(-w, l,n-1)

    forward(l)
    left(w)
    hilbert(w,l,n-1)

    forward(l)
    hilbert(w, l,n-1)

    left(w)
    forward(l)
    hilbert(-w,l,n-1)
    right(w)

r = 4  #Rekursionstiefe
a = 500
l0=a/(2**r-1)
penup()
setpos(-a/2.0,a/2.0)
pendown()
pensize(2)
tracer(False)
#speed(1)
#Winklel, Länge, Rekursionstiefe
hilbert(90,l0,r)
update()
mainloop()




