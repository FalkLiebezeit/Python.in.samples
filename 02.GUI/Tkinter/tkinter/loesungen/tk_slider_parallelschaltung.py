#tk_slider_parallelschaltung.py
import tkinter as tk                                                                     
main=tk.Tk()                                                                          
main.minsize(600,400)
main.title("Parallelschaltung mit drei Widerständen")
def ausgabe(self):
    U=sldU.get()
    R1=sldR1.get()
    R2=sldR2.get()
    R3=sldR3.get()
    I1=U/R1
    I2=U/R2
    I3=U/R3
    Ig=I1+I2+I3
    P1=U*I1
    P2=U*I2
    P3=U*I3
    Pg=U*Ig
    Ig=('{0:5.2f}'.format(Ig))
    I1=('{0:5.2f}'.format(I1))
    I2=('{0:5.2f}'.format(I2))
    I3=('{0:5.2f}'.format(I3))
    P1=('{0:5.2f}'.format(P1))
    P2=('{0:5.2f}'.format(P2))
    P3=('{0:5.2f}'.format(P3))
    Pg=('{0:5.2f}'.format(Pg))
    
    lblStrom["text"]="I=" + str(Ig) + " A"
    lblI1["text"] = "I1=" + str(I1) + " A"
    lblI2["text"] = "I2=" + str(I2) + " A"
    lblI3["text"] = "I3=" + str(I3) + " A"
    lblP1["text"] = "P1=" + str(P1) + " W"
    lblP2["text"] = "P2=" + str(P2) + " W"
    lblP3["text"] = "P3=" + str(P3) + " W"
    lblPg["text"] = "Pg=" + str(Pg) + " W"

sldU=tk.Scale(main, width=20, length=400,
              from_=0, to=200,
              resolution=1,
              tickinterval=20,
              label="Volt",
              command=ausgabe,
              font=("Arial 24"))

sldR1=tk.Scale(main, width=20, length=400,
              from_=10, to=100,
              resolution=1,
              tickinterval=10,
              label="R1",
              command=ausgabe,font=("Arial 24"))

sldR2=tk.Scale(main, width=20, length=400,
              from_=10, to=100,
              resolution=1,
              tickinterval=10,
              label="R2",
              command=ausgabe,font=("Arial 24"))
sldR3=tk.Scale(main, width=20, length=400,
              from_=10, to=100,
              resolution=1,
              tickinterval=10,
              label="R3",
              command=ausgabe,font=("Arial 24"))

lblStrom=tk.Label(main,text="I=",font=("Arial 24"))
lblI1=tk.Label(main,text="I1=",font=("Arial 24"))
lblI2=tk.Label(main,text="I2=",font=("Arial 24"))
lblI3=tk.Label(main,text="I3=",font=("Arial 24"))
lblPg=tk.Label(main,text="Pg=",font=("Arial 24"))
lblP1=tk.Label(main,text="P3=",font=("Arial 24"))
lblP2=tk.Label(main,text="P2=",font=("Arial 24"))
lblP3=tk.Label(main,text="P3=",font=("Arial 24"))
#Slider anordnen
sldU.grid(row=0,column=0)
sldR1.grid(row=0,column=1)
sldR2.grid(row=0,column=2)
sldR3.grid(row=0,column=3)
lblStrom.grid(row=1,column=0)
lblI1.grid(row=1,column=1)
lblI2.grid(row=1,column=2)
lblI3.grid(row=1,column=3)
lblPg.grid(row=2,column=0)
lblP1.grid(row=2,column=1)
lblP2.grid(row=2,column=2)
lblP3.grid(row=2,column=3)
main.mainloop()                                                                         

