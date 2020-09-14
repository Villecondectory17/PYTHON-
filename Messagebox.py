# Messageboxin tekeminen 
from tkinter import *
from tkinter import messagebox

root = TK()
root.title("Messagebox-harjoitus")

# Testaile messageboxin vaihtoehtoja: showinfo, showwarning, askquestion, asokcancel, asyesn
def popup(msg): 
    root = tkinter.Tk() 
    root.widthdraw() 
    popup = tk.Tk() 
    response = messagebox.askyesno("Messagebox haluaa sanoa: ", "Täällä ollaan")
    # Jos käyttäjä painaa Yes:
    if response == 1:
        Label(root, text="Painoit Yes-nappia!").pack()
    # Jos käyttäjä painaa No:
    else: 
        Label(root, text="Painoit No-nappia!").pack()
        
        messagebox.showinfo("Info") 
        messagebox.showwarning("Warning")
        messagebox.askquestion("question")
        messagebox.askokcancel("okcancel")
        messagebox.asyesn("")
    
# Nappula, joka kutsuu funktiota popup 
Button(root, text="Viesti", command=popup).pack()
root.mainloop() 
