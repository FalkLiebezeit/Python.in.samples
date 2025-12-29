import tkinter as tk

#Funktion für Trägheitsmoment  
def traegheitsmoment():
    pi=3.14159
    rho=7.85 #Dichte von Stahl kg/dm^3
    d = float(txtDurchmesser.get()) #dm
    l = float(txtLaenge.get())      #dm
    try:
        J = rho*l*pi*d**4/32
        J = ('{0:6.3f}'.format(1e-2*J)) #kgm^2
        lblErgebnis["text"] = "J=" + str(J) + " kgm^2"
    except:
        lblErgebnis["text"]= "Zahlen eingeben"
#Grafikbereich
main = tk.Tk('red')
main.minsize(400,200)
main.title("Trägheitsmoment eines Zylinders")
#Label erzeugen
lblDurchmesser=tk.Label(main, text="Durchmesser in dm eingeben")
lblLaenge=tk.Label(main, text="Länge in dm eingeben")
lblErgebnis = tk.Label(main,text="")
#Textfelder erzeugen
txtDurchmesser=tk.Entry(main, width=5,justify="right")
txtDurchmesser.insert(5,"0.8")
txtLaenge = tk.Entry(main,width=5, justify="right")
txtLaenge.insert(5,"10")
#Befehlschaltflächen erzeugen
cmdBerechnen=tk.Button(main, text="Berechnen", command=traegheitsmoment)
cmdEnde=tk.Button(main, text="Beenden", command=main.destroy)
#Steuerelemente einfügen
lblDurchmesser.pack()
txtDurchmesser.pack()
lblLaenge.pack()
txtLaenge.pack()
cmdBerechnen.pack()
lblErgebnis.pack()
cmdEnde.pack()
main.mainloop()

'''
lblDurchmesser.pack(side="left")
txtDurchmesser.pack(side="left")
lblLaenge.pack(side="left")
txtLaenge.pack(side="left")
cmdBerechnen.pack(side="left")
lblErgebnis.pack(side="left")
cmdEnde.pack(side="left")
'''

