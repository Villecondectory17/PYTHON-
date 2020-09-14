# Uuden ikkunan avaaminen 

from tkinter import *

root = Tk()

def open():
    top = Toplevel()
    top.title("Uusi ikkuna")
    closeWindowButton = Button(top, text="Sulje ikkuna", command=top.destroy).pack()
    
openWindowButton = Button(root, text="Avaa uusi ikkuna", command=open).pack()

root.mainloop()
