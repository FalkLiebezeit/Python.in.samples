#09_regelstrecke.py
import tkinter as tk
main = tk.Tk()
main.title("Regelstrecke 2. Ordnung")
xmax, ymax = 800, 400
canZ = tk.Canvas(width=xmax, height=ymax, bg='white')
#Bezeichnungsfelder
lblR=tk.Label(main, text="R")
lblL = tk.Label(main, text="L")
lblMn=tk.Label(main, text="Mn")
lblIa=tk.Label(main, text="Ia")
lblJ=tk.Label(main, text="J")
lblTmax=tk.Label(main, text="tmax")
#Textfelder
txtR=tk.Entry(main, width=5)
txtR.insert(5,"1.5")
txtL=tk.Entry(main, width=5)
txtL.insert(5,"24")
txtMn=tk.Entry(main, width=5)
txtMn.insert(5,"170")
txtIa=tk.Entry(main, width=5)
txtIa.insert(5,"40")
txtJ=tk.Entry(main, width=5)
txtJ.insert(5,"0.22")
txtTmax=tk.Entry(main, width=5)
txtTmax.insert(5,"300")

def loesche():
    return canZ.delete("all")
    
def strecke():
    w = ymax/2
    U1 = w
    R = float(txtR.get())
    L = float(txtL.get())
    J = float(txtJ.get())
    Ia = float(txtIa.get())
    Mn = float(txtMn.get())
    tmax=float(txtTmax.get())
    C=1e3*J*(Ia/Mn)**2
    u2=i=t = 0
    dt = 0.5
    sx=xmax/tmax
    u2_t = []
    canZ.create_line(0, w, xmax, w, fill='green', width=2)
    while t<=tmax:        
        i = i + (U1-R*i-u2)*dt/L
        u2 = u2 + i*dt/C
        t=t+dt
        u2_t.append(int(sx*t))
        u2_t.append(int(-u2) + ymax)
    canZ.create_line(u2_t, fill='blue', width=2)
#Befehlsschaltflächen
cmdStart=tk.Button(main, text="Start", command=strecke)
cmdNeu = tk.Button(main, text="Neu", command=loesche)
cmdEnde=tk.Button(main, text="Beenden", command=main.destroy)
#Steuerelemente anordnen
canZ.pack()
lblR.pack(side="left")
txtR.pack(side="left")
lblL.pack(side="left")
txtL.pack(side="left")
lblMn.pack(side="left")
txtMn.pack(side="left")
lblIa.pack(side="left")
txtIa.pack(side="left")
lblJ.pack(side="left")
txtJ.pack(side="left")
lblTmax.pack(side="left")
txtTmax.pack(side="left")
cmdStart.pack(side="left")
cmdNeu.pack(side="left")
cmdEnde.pack(side="left")
main.mainloop()