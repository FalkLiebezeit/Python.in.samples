#L_11_01.py
import tkinter as tk
main = tk.Tk()
main.title("Traegheitsmoment eines Zylinders")
main.minsize(400,200)
rho=7.85 #Dichte von Stahl
    
def zylinder():
    d = float(txtDurchmesser.get())
    l = float(txtLaenge.get())
    try:
        V = 0.785*d**2*l
        m = rho*V
        O = 2**0.785*d**2+3.1416*d*l
        V = ('{0:6.2f}'.format(V))
        m = ('{0:6.2f}'.format(m))
        O = ('{0:6.2f}'.format(O))
        lblV["text"] = "Volumen=" + str(V) + " dm^3"
        lblm["text"] = "Masse=" + str(m) + " kg"
        lblO["text"] = "Oberfläche=" + str(O) + " dm^2"
    except:
        lblV["text"]= "Zahlen eingeben"
        lblm["text"]= "Zahlen eingeben"
        lblO["text"]= "Zahlen eingeben"

#Label erzeugen
lblDurchmesser=tk.Label(main, text="Durchmesser in dm eingeben")
lblLaenge=tk.Label(main, text="Laenge in dm eingeben")
lblV = tk.Label(main,text="")
lblm = tk.Label(main,text="")
lblO = tk.Label(main,text="")
#Textfelder erzeugen
txtDurchmesser=tk.Entry(main, width=5,justify="right")
txtDurchmesser.insert(5,"0.8")
txtLaenge = tk.Entry(main,width=5, justify="right")
txtLaenge.insert(5,"10")
#Befehlschaltflächen erzeugen
cmdBerechnen=tk.Button(main, text="Berechnen",command=zylinder)
cmdEnde=tk.Button(main, text="Benden",command=main.destroy)
#Steuerelemente einfügen
lblDurchmesser.pack()
txtDurchmesser.pack()
lblLaenge.pack()
txtLaenge.pack()
cmdBerechnen.pack()
lblV.pack()
lblm.pack()
lblO.pack()
cmdEnde.pack()
main.mainloop()
