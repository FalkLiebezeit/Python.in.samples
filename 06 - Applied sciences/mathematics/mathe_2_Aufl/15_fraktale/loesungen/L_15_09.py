#L_15_08.py
#Sierpinski-Teppich
from turtle import *
m=3
def teppich(a,n):
    if n < 1:
        color('blue')
        begin_fill()
        for _ in range (4):
            forward(a)
            left(90)
        end_fill()
    else:
        for _ in range(4):
            teppich(a/3,n-1)    
            forward(a/3)
            teppich(a/3,n-1)    
            forward(a/3)
            forward(a/3)
            left(90)

tracer(False)
penup()
setpos(-200,-200)
pendown()
teppich(400,m)
update()
mainloop()