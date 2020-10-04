# Avaa UI kirjasto 
from tkinter import *

# Tk() = uusi ikkuna. Sijoitetaan se muuttujaan root.
root = Tk()

# Funktio nappulan painamisen käsittelyyn.
def IClicked():
    # Kirjoita tekstit Labeliin, joka sijoitetaan ikkunaan, nimeltä root.
    buttonClickLabel=Label(root, text="Nappulaa painettu")
    buttonClick.pack()


# Esimerkki disabled nappulasta.
disabledButton = Button(root, text="Paina nappulaa", state=DISABLED)
disabledButton.pack()


# Esimerkki disabled nappulasta.
disabledButton = Button(root, text="Paina nappulaa", state=DISABLED)
disabledButton.pack()

# Esimerkki aktiivisesta nappulasta.
activeButton = Button(root, text="Paina nappulaa", padx=50, pady=50, command=IClicked, fg="red")
activeButton.pack()

# Käynnistä root niminen ikkuna.
root.mainloop()