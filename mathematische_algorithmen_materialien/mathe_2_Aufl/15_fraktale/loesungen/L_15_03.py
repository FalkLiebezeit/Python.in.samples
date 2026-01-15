#L_15_03.py
#Dreieck + Quadrat
from math import sqrt
from turtle import *

def haus(c):
    a=c/sqrt(2)
    right(45)
    forward(a)
    right(45)
    forward(c)
    right(90)
    forward(c)
    right(90)
    forward(c)
    right(45)
    forward(a)
        
penup()
setpos(0,200)
pendown()
pensize(2)
haus(200)
mainloop()