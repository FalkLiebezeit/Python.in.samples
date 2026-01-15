#10_pidregler.py
import tkinter as tk
main = tk.Tk()
main.title("Sprungantwort von P-, PI- und PID-Regler")
xmax, ymax = 800,400
ausw=tk.StringVar()
ausw.set("PID")
canZ = tk.Canvas(width=xmax, height=ymax, bg='white')

def loesche():
    return canZ.delete("all")

def regler():
    tmax=400
    Kp=50
    Tn=50
    Tv=50
    e=1
    t=ui=e0=ur=0
    dt=2
    sx=xmax/tmax
    u2_t = []
    while t<=tmax:       
        up = Kp*e #P-Regler
        ui = ui + Kp*e*dt/Tn #PI-Regler
        ud = Kp*Tv*(e-e0)/dt #PD-Regler
        e0=e  
        t=t+dt       
        if ausw.get()=="P":     ur=up
        elif ausw.get()=="PI":  ur= up+ui
        elif ausw.get()=="PID": ur=up+ui+ud
        u2_t.append(sx*t)
        u2_t.append(int(-ur) + ymax)  
    canZ.create_line(u2_t, fill='blue', width=2)
optP=tk.Radiobutton(main,text="P-Regler",variable=ausw,value="P")
optPI=tk.Radiobutton(main,text="PI-Regler",variable=ausw,value="PI")
optPID=tk.Radiobutton(main,text="PID-Regler",variable=ausw,value="PID")
cmdStart = tk.Button(main,text="Start",command=regler)
cmdNeu=tk.Button(main,text="Neu",command=loesche)
canZ.pack()
optP.pack(side="left")
optPI.pack(side="left")
optPID.pack(side="left")
cmdStart.pack(side="left")
cmdNeu.pack(side="left")
main.mainloop()