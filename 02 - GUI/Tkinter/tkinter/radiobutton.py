#04_radiobutton.py
import tkinter as tk

def rechne():
    m=1   #Masse in kg
    r=0.5 #Radius in m
    Jp = m*r**2     #Punktmasse
    Jz = 0.5*m*r**2 #Vollzylinder
    Jk = 2./5.*m*r**2 #Kugel    
    if ausw.get()=="pm":
        lblErgebnis["text"]=str(Jp)+" kgm^2"
    elif ausw.get()=="vz":
        lblErgebnis["text"]=str(Jz)+" kgm^2"
    elif ausw.get()=="vk":
        lblErgebnis["text"]=str(Jk)+" kgm^2"
#Grafikbereich
main = tk.Tk()
main.minsize(580,50)
main.title("Auswahl mit Radiobutton")
ausw=tk.StringVar()
ausw.set("vz")
#Steuerelemente erzeugen       
optPm=tk.Radiobutton(main,text="Punktmasse",variable=ausw,value="pm")
optVz=tk.Radiobutton(main,text="Vollzylinder",variable=ausw,value="vz")
optVk=tk.Radiobutton(main,text="Kugel",variable=ausw,value="vk")
lblJ=tk.Label(main, text="J=")
lblErgebnis = tk.Label(main,text="")
cmdStart = tk.Button(main, text="Berechnen",command=rechne)
cmdEnde=tk.Button(main,text="Ende",command=main.destroy)
#Steuerelemente anzeigen
optPm.pack(side="left")
optVz.pack(side="left")
optVk.pack(side="left")
cmdStart.pack(side="left")
cmdEnde.pack(side="left")
lblJ.pack(side="left")
lblErgebnis.pack(side="left")
main.mainloop()
