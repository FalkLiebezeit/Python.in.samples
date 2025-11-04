import tkinter as tk

#Funktion für Trägheitsmoment
def traegheitsmoment():
    pi=3.14159
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
main.minsize(400,115)
lblDurchmesser=tk.Label(main, text="Durchmesser in dm eingeben")
lblLaenge=tk.Label(main, text="Länge in dm eingeben")
lblTraegheitsmoment = tk.Label(main,text="Trägheitsmoment")
lblErgebnis = tk.Label(main,text="")
txtDurchmesser=tk.Entry(main, justify="right")
txtDurchmesser.insert(2,"0.8")
txtLaenge = tk.Entry(main, justify="right")
txtLaenge.insert(2,"10")
cmdBerechnen=tk.Button(main, text="Berechnen",command=traegheitsmoment)
cmdEnde=tk.Button(main, text="Beenden", command=main.destroy)
lblDurchmesser.grid(row=0,column=0,sticky="w")
txtDurchmesser.grid(row=0,column=1,sticky="e")
lblLaenge.grid(row=1,column=0,sticky="w")
txtLaenge.grid(row=1,column=1,sticky="e")
lblTraegheitsmoment.grid(row=2,column=0,sticky="w")
lblErgebnis.grid(row=2,column=1,sticky="e")
cmdBerechnen.grid(row=3,column=0)
cmdEnde.grid(row=3,column=1)
main.mainloop()