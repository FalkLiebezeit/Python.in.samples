#11_regelkreis1.py
import tkinter as tk
main = tk.Tk()
main.title("PID-Regler mit Strecke 2. Ordnung")
xmax, ymax = 800,400
canZ = tk.Canvas(width=xmax, height=ymax, bg='white')
U1=100.0
R,L=1,25
I,M,J = 40,170,1
C=1e3*J*(I/M)**2
tmax=250
Kp=5
Tn=50
Tv=10
t=i=y=ui=e=e0=0.0
w=ymax/2
dt=0.25
sx=xmax/tmax
u2_t = []
while t<=tmax:    
    e=w-y
    up = Kp*e
    ud = Kp*Tv*(e-e0)/dt
    e0=e
    ui = ui + Kp*e*dt/Tn
    U1 = up + ui + ud
    i = i + (U1-R*i-y)*dt/L
    y = y + i*dt/C
    t=t+dt
    u2_t.append(sx*t)
    u2_t.append(-y + ymax)  
canZ.create_line(u2_t, fill='blue', width=2)
canZ.create_line(0, w, xmax, w, fill='red', width=2)
canZ.pack()
main.mainloop()