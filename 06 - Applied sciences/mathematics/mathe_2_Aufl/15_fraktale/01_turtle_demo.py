#01_turtle_demo.py
from turtle import *
a,b=300,200
x1,y1=-a/2,b/2
phi=90 #Winkel
title("Turtle Demonstration")
setup(width=480, height=320)
penup()
setpos(x1,y1)
pendown()
pensize(2)
speed(1) #1 bis 10
forward(a)
right(phi)
forward(b)
right(phi)
forward(a)
right(phi)
forward(b)
right(phi)
mainloop()
