#gui_frame.py
#Demonstration der frame-Methode
from math import pi
import tkinter as tk

def traegheitsmoment():
    rho=7.85 #kg/dm^3
    d = float(txtDurchmesser.get())
    l = float(txtLaenge.get())
    try:
        J = rho*l*pi*d**4/32
        J = ('{0:6.3f}'.format(1e-2*J)) #Umrechnung in kgm^2
        lblErgebnis["text"] = str(J) + " kgm^2"
    except:
        lblErgebnis["text"]= "Zahlen eingeben"
#Grafikbereich
main = tk.Tk()
main.title("Trägheitsmoment eines Zylinders")
#main.minsize(400,200)
frmLinks=tk.Frame(main,relief="sunken",bd=3)
frmRechts=tk.Frame(main,relief="groove",bd=3)
lblDurchmesser=tk.Label(frmLinks, text="Durchmesser in dm eingeben")
lblLaenge=tk.Label(frmLinks, text="Laenge in dm eingeben")
lblTraegheitsmoment = tk.Label(frmLinks,text="Traegheitsmoment")
lblErgebnis = tk.Label(frmRechts,text="")
txtDurchmesser=tk.Entry(frmRechts, justify="right")
txtDurchmesser.insert(5,"0.8")
txtLaenge = tk.Entry(frmRechts, justify="right")
txtLaenge.insert(5,"10")
cmdBerechnen=tk.Button(frmLinks, text="Berechnen", command=traegheitsmoment)
cmdEnde=tk.Button(frmRechts, text="Beenden", command=main.destroy)
frmLinks.pack(side="left",padx=10,pady=10,expand=1,fill="both")
frmRechts.pack(side="right",padx=10,pady=10,expand=1,fill="both")
lblDurchmesser.pack()
lblLaenge.pack()
lblTraegheitsmoment.pack()
txtDurchmesser.pack()
txtLaenge.pack()
lblErgebnis.pack()
cmdBerechnen.pack()
cmdEnde.pack()
main.mainloop()