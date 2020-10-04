import tkinter 
from tkinter import *
from tkinter import messagebox 
from tkinter.ttk import *

val = 0 
def clicked():
    global val
    if (val < 5):
        val = val + 1
        var.set(val)
        lbl.config(text="Pressed "+str(val)+" out of 5 Times.")
    else:
        messagebox.showwarning("Warning", "You already pressed 5 times !") 

root = tkinter.Tk()
root.geometry("500x500")


var = IntVar()
var.set(0)
pgbar = Progressbar(
    root, 
    orient = HORIZONTAL,
    mode = 'determinate',
    maximum = 5,
    length = 200,
    variable = var,
)
pgbar.pack(pady=40)

btn = Button(
    root,
    text = "Click me 5 times", 
    command = clicked, 

) 
btn.pack(pady=20)

lbl = Label(
    root,
    font = ("Consolas",16),
)
lbl.pack()
root.mainloop() 