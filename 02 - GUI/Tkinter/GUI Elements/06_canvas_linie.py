import tkinter as tk

main = tk.Tk()

xmax,ymax=500,500
canZ = tk.Canvas(width=xmax, height=ymax, bg='white')
canZ.create_line(0,ymax/2,xmax, ymax/2, fill='black', width=3)
canZ.create_line(0,0,xmax, ymax, fill='blue', width=3)
canZ.pack()
main.mainloop()