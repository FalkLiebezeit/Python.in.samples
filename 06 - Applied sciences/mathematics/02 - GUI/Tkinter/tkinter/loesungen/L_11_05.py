#16_regelkreis2.py
import tkinter as tk
main = tk.Tk()
main.title("Regelkreis mit Strecke 2. Ordnung")
xmax, ymax = 1000,600
w=ymax/2 #Führungsgröße
rd=4     #Rand
ausw=tk.StringVar()
ausw.set("S")
main.minsize(xmax,ymax)
main.resizable(False,False)

def rahmen():
    canZ.create_line(0,w,xmax,w,fill='red',width=2)
    canZ.create_line(rd,rd,xmax,rd,fill="black",width=2)
    canZ.create_line(rd,ymax,xmax,ymax,fill="black",width=2)
    canZ.create_line(rd,0,rd,ymax,fill="black",width=2)
    canZ.create_line(xmax, rd, xmax, ymax,fill="black",width=2)

def loesche():
    return canZ.delete("all"),rahmen()

def koordinate(event):
    tmax=float(txtTmax.get())
    x, y = event.x, event.y
    x, y = tmax*x/xmax-2, 100*(ymax-y)/w
    x, y = ('{0:3.0f}'.format(x)), ('{0:3.0f}'.format(y))
    lblKoordinate["text"]="t:"+str(x)+" ms  y:"+str(y)+"%" 

def regelkreis():
    tmax=float(txtTmax.get())
    Kp =float(txtKp.get())
    Tn =float(txtTn.get())
    Tv =float(txtTv.get())
    R = float(txtR.get())
    L = float(txtL.get())
    J = float(txtJ.get())
    Ia= float(txtIa.get())
    Mn= float(txtMn.get())
    C=1.0e3*J*(Ia/Mn)**2
    t=y=ui=ud=i=e=e0=0
    dt=0.05
    sx=xmax/tmax
    u2_t = []
    while t<=tmax-rd/2:
        e=w-y
        up = Kp*e
        ui = ui + Kp*e*dt/Tn
        ud = Kp*Tv*(e-e0)/dt
        e0=e
        if ausw.get()=="P":     ur=up
        elif ausw.get()=="PD":  ur=up+ud
        elif ausw.get()=="PI":  ur=up+ui
        elif ausw.get()=="PID": ur=up+ui+ud
        elif ausw.get()=="S":   ur=w
        i = i + (ur-R*i-y)*dt/L
        y = y + i*dt/C
        t=t+dt
        u2_t.append(int(sx*t)+rd)
        u2_t.append(int(-y)+ymax)        
    canZ.create_line(u2_t,fill='blue',width=2)    

#Zeichenfläche 1. Zeile
canZ = tk.Canvas(width=xmax,height=ymax,bg='white')
canZ.grid(row=0,column=0,columnspan=5)
rahmen()
#Auswahl der Regler 2. Zeile
optS=tk.Radiobutton(main,text="Strecke",variable=ausw,value="S")
optS.grid(row=1,column=0,sticky="w")
optP=tk.Radiobutton(main,text="P-Regler",variable=ausw,value="P")
optP.grid(row=1,column=1,sticky="w")
optPD=tk.Radiobutton(main,text="PD-Regler",variable=ausw,value="PD")
optPD.grid(row=1,column=2,sticky="w")
optPI=tk.Radiobutton(main,text="PI-Regler",variable=ausw,value="PI")
optPI.grid(row=1,column=3,sticky="w")
optPID=tk.Radiobutton(main,text="PID-Regler",variable=ausw,value="PID")
optPID.grid(row=1,column=4,sticky="w")
#Ankerwiderstand 1. Spalte
tk.Label(main, text="R in Ohm").grid(row=2,column=0,sticky="w")
txtR=tk.Entry(main, width=5)
txtR.insert(5,"1.5")
txtR.grid(row=2,column=1,sticky="w")
#Ankerinduktivität
tk.Label(main, text="L in mH").grid(row=3,column=0,sticky="w")
txtL=tk.Entry(main, width=5)
txtL.insert(5,"24")
txtL.grid(row=3,column=1,sticky="w")
#Bemessungsmoment
tk.Label(main, text="Mn in Nm").grid(row=4,column=0,sticky="w")
txtMn=tk.Entry(main, width=5)
txtMn.insert(5,"172")
txtMn.grid(row=4,column=1,sticky="w")
#Bemessungstrom
tk.Label(main, text="Ia in A").grid(row=5,column=0,sticky="w")
txtIa=tk.Entry(main, width=5)
txtIa.insert(5,"41")
txtIa.grid(row=5,column=1,sticky="w")
#Trägkeitsmoment
tk.Label(main, text="J in kgm^2").grid(row=6,column=0,sticky="w")
txtJ=tk.Entry(main, width=5)
txtJ.insert(5,"1")
txtJ.grid(row=6,column=1,sticky="w")
#Verstärkung des Reglers 3. Spalte
tk.Label(main, text="Kp").grid(row=2,column=2,sticky="w")
txtKp=tk.Entry(main, width=5)
txtKp.insert(5,"5")
txtKp.grid(row=2,column=3,sticky="w")
#Nachstellzeit
tk.Label(main, text="Tn in ms").grid(row=3,column=2,sticky="w")
txtTn=tk.Entry(main, width=5)
txtTn.insert(5,"50")
txtTn.grid(row=3,column=3,sticky="w")
#Vorhaltezeit
tk.Label(main, text="Tv in ms").grid(row=4,column=2,sticky="w")
txtTv=tk.Entry(main, width=5)
txtTv.insert(5,"5")
txtTv.grid(row=4,column=3,sticky="w")
#Koordinaten
tk.Label(main, text="tmax").grid(row=5,column=2,sticky="w")
txtTmax=tk.Entry(main, width=5)
txtTmax.insert(5,"250")
txtTmax.grid(row=5,column=3,sticky="w")
tk.Label(main, text="Koordinate").grid(row=6,column=2,sticky="w")
lblKoordinate=tk.Label(main,width=15)
lblKoordinate.grid(row=6,column=3,sticky="w")
#Befehlschaltflächen
tk.Button(main,text="Start",command=regelkreis,width=7).grid(row=2,column=4,sticky="w")
tk.Button(main,text="Neu",command=loesche,width=7).grid(row=3,column=4,sticky="w")
tk.Button(main,text="Beenden",command=main.destroy,width=7).grid(row=4,column=4,sticky="w")
canZ.bind('<Motion>', koordinate)
main.mainloop()
