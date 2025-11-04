#L_11_03.py
import tkinter as tk                                                                     
main=tk.Tk()                                                                          
main.minsize(400,400)
main.title("Reihenschaltung mit drei Widerständen")
font="Arial 14"

def ausgabe(self):
    U=sldU.get()
    R1=sldR1.get()
    R2=sldR2.get()
    R3=sldR3.get()
    Rg=R1+R2+R3
    I=U/Rg
    U1=R1*I
    U2=R2*I
    U3=R3*I
    I=('{0:5.2f}'.format(I))
    U1=('{0:5.2f}'.format(U1))
    U2=('{0:5.2f}'.format(U2))
    U3=('{0:5.2f}'.format(U3))
    lblStrom["text"]= "I=" + str(I) + " A"
    lblU1["text"] = "U1=" + str(U1) + " V"
    lblU2["text"] = "U2=" + str(U2) + " V"
    lblU3["text"] = "U3=" + str(U3) + " V"
#Slider
sldU=tk.Scale(main, width=20, length=400,
              from_=0, to=200,
              resolution=1,
              tickinterval=20,
              label="Volt",
              command=ausgabe,
              font=(font))    
sldR1=tk.Scale(main, width=20, length=400,
              from_=10, to=100,
              resolution=1,
              tickinterval=10,
              label="R1",
              command=ausgabe,font=(font))

sldR2=tk.Scale(main, width=20, length=400,
              from_=10, to=100,
              resolution=1,
              tickinterval=10,
              label="R2",
              command=ausgabe,font=(font))
sldR3=tk.Scale(main, width=20, length=400,
              from_=10, to=100,
              resolution=1,
              tickinterval=10,
              label="R3",
              command=ausgabe,font=(font))
#Grafikbereich
lblStrom=tk.Label(main,text="I=",font=(font))
lblU1=tk.Label(main,text="U1=",font=(font))
lblU2=tk.Label(main,text="U2=",font=(font))
lblU3=tk.Label(main,text="U3=",font=(font))
#Slider anordnen
sldU.grid(row=0,column=0)
sldR1.grid(row=0,column=1)
sldR2.grid(row=0,column=2)
sldR3.grid(row=0,column=3)
lblStrom.grid(row=1,column=0)
lblU1.grid(row=1,column=1)
lblU2.grid(row=1,column=2)
lblU3.grid(row=1,column=3)
main.mainloop()                                                                         
