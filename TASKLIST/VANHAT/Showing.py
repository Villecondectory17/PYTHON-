from tkinter import *

fenster = Tk() 
fenster.title("Unser GUI Programm") 
fenster.geometry("300x300")
 
def ausgabe():
    print ("Hello World!") 


knopf1 = Button(fenster, text="Klick mich!",command=ausgabe) 
knopf1.pack()

eingabe = Entry(fenster)
eingabe.pack()

label1 = Label(fenster)   
label1.pack

class Test():
    def __init__(self):
        print ("Ich wurde erzeugt")

def rechnen():
    objekt = Test() 
    try:
        x = float(eingabe.get()) 
    except: 
        label1.configure(text="Bitte eine Zahl eingeben!")
    try:    
        label1.configure(text=(x**0.5))
    except:
        print ("Bitte ein Zahl eingeben!") 

        #print (eingabe.get())
        #float(eingabe.get())

knopf2 = Button(fenster, text="Ich lese",command=rechnen) 
knopf2.pack() 

mainloop()


