#L_11_04.py
import tkinter as tk
main = tk.Tk()
main.title("PID-Regler mit Strecke 3. Ordnung")
xmax, ymax = 800,400
canZ = tk.Canvas(width=xmax, height=ymax, bg='white')
U1=100.0
R1,C1=1,1
R2,C2=1,2
R3,C3=1,3
T1=R1*C1
T2=R2*C2
T3=R3*C3
tmax=20
Kp=5
Tn=8
Tv=1
t=y=ui=e=e0=0
u2=u3=u4=0
w=ymax/2
dt=0.05
sx=xmax/tmax
u2_t = []
#PID-Regler
def regler(e):
    global e0,ui
    up = Kp*e
    ud = Kp*Tv*(e-e0)/dt
    e0=e
    ui = ui + Kp*e*dt/Tn
    ur=up+ud+ui
    return ur
#Regelstrecke 3.Ordnung
def strecke(u1):
    global u2,u3,u4
    u2 = u2 + (u1-u2)*dt/T1
    u3 = u3 + (u2-u3)*dt/T2
    u4 = u4 + (u3-u4)*dt/T3
    return u4
#Regelkreis    
while t<=tmax:    
    e=w-y
    u1=regler(e)
    #y=strecke(w) #nur Strecke
    y=strecke(u1) #mit Regelung
    t=t+dt
    u2_t.append(sx*t)
    u2_t.append(-y + ymax)  
canZ.create_line(u2_t, fill='blue', width=2)
canZ.create_line(0, w, xmax, w, fill='red', width=2)
canZ.pack()
main.mainloop()
