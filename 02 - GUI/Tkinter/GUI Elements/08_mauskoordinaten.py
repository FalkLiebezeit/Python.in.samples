#08_mauskoordinaten.py
import tkinter as tk
import math as m
main = tk.Tk()
xmax, ymax = 500, 500
x1,x2 = 0, 10
y1,y2 =-10, 10
ym=ymax/2
sx=(x2-x1)/xmax
sy=ymax/(y2-y1)
canZ = tk.Canvas(width=xmax, height=ymax, bg='white')
canZ.create_line(0,ym,xmax,ym,fill='black',width=2)

def f(x):
    return 8*m.sin(x)

def koordinate(e):
    x, y = e.x, e.y
    x, y = sx*x, (0.5*ymax-y)/sy
    x, y = ('{0:4.1f}'.format(x)), ('{0:4.1f}'.format(y))
    lblKoordinate["text"]='  x: '+str(x)+' y: '+str(y)

def zeichne():
    dx=1
    x=0
    while x<=xmax:
        canZ.create_line(x,-sy*f(sx*x)+ym,(x+1),\
        -sy*f(sx*(x+1))+ym,fill='blue',width=2)
        x=x+dx

lblKoordinate=tk.Label(main, text="")
cmdStart=tk.Button(main, text="Zeichne", command=zeichne)
canZ.pack()
cmdStart.pack(side="left")
lblKoordinate.pack(side="left")
canZ.bind("<Motion>", koordinate)
main.mainloop()