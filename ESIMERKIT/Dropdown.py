# Dropdown esimerkki 

from tkinter import *

root = Tk()
root.title("Alasvetovalikko")
root.geometry("400x400") 

options=[
    "ensimmäinen",
    "Toinen",
    "Kolmas",
    "Neljäs",
    "Viides"
]

selectItem = StringVar()
selectItem.set(options[0])

def show():
    myLabel=Label(root, text=selectItem.get()).pack()
    
drop = Optionmenu(root, selectItem, *options
drop.pack(root, text fill = BOTH, expand = True)
                  
myButton = Button(root, text="Valitse tästä", command=show).pack()
myButton.pack(fill = BOTH, expand = True)
                 
root.mainloop()
  
  
