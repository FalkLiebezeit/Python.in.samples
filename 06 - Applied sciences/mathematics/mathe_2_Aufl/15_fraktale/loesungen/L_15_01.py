#L_15_01.py
#Quadrat zeichnen
from turtle import *
a=200
x1=-a/2
y1=a/2
phi=90
penup()
setpos(x1,y1)
pendown()
pensize(2)
for _ in range(4):
    forward(a)
    right(phi)
mainloop()

