#L_15_02.py
#gleichseitiges Dreieck zeichnen
from turtle import *
a=400
x1=-a/2
y1=-a/3
penup()
setpos(x1,y1)
pendown()
pensize(2)
for phi in [60,-120,-120]:
    left(phi)
    forward(a)
mainloop()