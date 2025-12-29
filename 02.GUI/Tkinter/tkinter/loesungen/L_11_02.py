#L_11_02.py
import tkinter as tk                                                                     
main=tk.Tk()                                                                          
main.minsize(500,200)
font="Arial 14"

def strom(self):
    U=sldU.get()
    R=sldR.get()
    I=U/R
    I=('{0:5.2f}'.format(I))
    lblStrom["text"] = "I=" + str(I) + " A"

sldU=tk.Scale(main, width=20, length=400,
              from_=0, to=200,
              orient='horizontal',
              resolution=1,
              tickinterval=20, 
              label="U in V",    
              command=strom,   #Funktionsaufruf
              font=(font))    
sldR=tk.Scale(main, width=20, length=400,
              from_=10, to=100,
              orient='horizontal',
              resolution=1,
              tickinterval=10,
              label=" R in Ohm",
              command=strom,   #Funktionsaufruf
              font=(font))

main.title("Stromstärke im einfachen Stromkreis")
sldU.set(20) #Initialisierung
lblStrom=tk.Label(main,text="I=",font=(font))
lblStrom.pack()
sldU.pack()
sldR.pack()
main.mainloop()                                                                         