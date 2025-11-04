#gui_place.py
#Demonstration der place-Methode
from math import pi
import tkinter as tk

def traegheitsmoment():
    rho=7.85 #kg/dm^3
    d = float(txtDurchmesser.get())
    l = float(txtLaenge.get())
    try:
        J = rho*l*pi*d**4/32
        J = ('{0:6.3f}'.format(J/100.)) #Umrechnung in kgm^2
        lblErgebnis["text"] = str(J) + " kgm^2"
    except:
        lblErgebnis["text"]= "Zahlen eingeben"
#Grafikbereich
main = tk.Tk()
main.title("Trägheitsmoment eines Zylinders")
lblDurchmesser=tk.Label(main, text="Durchmesser in dm eingeben")
lblLaenge=tk.Label(main, text="Laenge in dm eingeben")
lblTraegheitsmoment = tk.Label(main,text="Traegheitsmoment")
lblErgebnis = tk.Label(main,text="")
txtDurchmesser=tk.Entry(main, width=10,justify="right")
txtDurchmesser.insert(5,"0.8")
txtLaenge = tk.Entry(main,width=10, justify="right")
txtLaenge.insert(5,"10")
cmdBerechnen=tk.Button(main, text="Berechnen", command=traegheitsmoment)
cmdEnde=tk.Button(main, text="Beenden", command=main.destroy)
main.minsize(400,200)
main.resizable(False,False)
x1,x2=10, 390
y1,y2,y3,y4=20,50,80,110
lblDurchmesser.place(x=x1,y=y1, anchor="w")
lblLaenge.place(x=x1,y=y2, anchor="w")
txtDurchmesser.place(x=x2,y=y1, anchor="e")
txtLaenge.place(x=x2,y=y2, anchor="e")
lblTraegheitsmoment.place(x=x1,y=y3, anchor="w")
lblErgebnis.place(x=x2,y=y3, anchor="e")
cmdBerechnen.place(x=x1,y=y4, anchor="w")
cmdEnde.place(x=x2,y=y4, anchor="e")
main.mainloop()