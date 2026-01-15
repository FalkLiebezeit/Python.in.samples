#07_skalierung.py
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
    
def zeichne():
    dx=1
    x=0
    while x<=xmax:
        canZ.create_line(x,-sy*f(sx*x)+ym,(x+1),\
        -sy*f(sx*(x+1))+ym,fill='blue',width=2)
        x=x+dx

cmdStart=tk.Button(main, text="Zeichne", command=zeichne)
canZ.pack()
cmdStart.pack()
main.mainloop()