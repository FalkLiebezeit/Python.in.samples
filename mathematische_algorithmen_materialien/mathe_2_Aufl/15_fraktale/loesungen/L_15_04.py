#L_15_04.py
#Koch-Kurve mit rechtsdrehenden Winkeln
from turtle import  *

def koch(l, n):
    if n == 0:
        p.forward(l)
    else:
        for phi in [0, 300, 120, 300]:
            p.right(phi)
            koch(l/3,n-1) #Rekursion
wn = Screen()
wn.bgcolor("white")
wn.setup(width = 640, height = 640)
wn.title("Koch-Kurve")
p = Turtle()
p.pencolor("red")
p.pensize(2)
p.penup()
p.setpos(-200,100)
p.pendown()
p.speed(10)
n = 3
l1=400
wn.tracer(False)
koch(l1, n)
p.right(120)
koch(l1, n)
p.right(120)
koch(l1, n)
wn.update()
wn.mainloop()

