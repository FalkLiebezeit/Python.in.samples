#05_slider.py
import tkinter as tk                                                                     
main=tk.Tk()
#Trägheitsmoment 
def traegheitsmoment(self):
    pi=3.14159
    rho=7.85 #Dichte von Stahl kg/dm^3
    l=10     #Länge des Zylinders in dm
    d=sldD.get() #Durchmesser in mm
    d=1e-2*d #Umwandlung in dm
    J = rho*l*pi*d**4/32 #in kgdm^2
    J=('{0:5.3f}'.format(1e-2*J))  #Umwandlung in kgm^2
    lblD["text"] = "J=" + str(J) + " kgm^2"
#Slider-Objekt erzeugen
sldD=tk.Scale(main, width=20, length=400,
              from_= 50, to= 200,  #Bereich in mm
              orient='horizontal',
              resolution=1,        #Auflösung in mm
              tickinterval=25, 
              label="d in mm",    
              command=traegheitsmoment, #Funktionsaufruf
              font=("Arial 14"))    
#Grafikbereich                                                                        
main.minsize(500,110)
main.title("Trägheitsmoment eines Zylinders")
lblD=tk.Label(main,text="J=",font=("Arial 14"))
sldD.set(80) #Anfangswert setzen
lblD.pack()
sldD.pack()
lblD.pack()
main.mainloop()                                                                         
