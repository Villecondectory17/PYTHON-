from tkinter import *
from tkinter import ttk

win = Tk()

wrapper1 = LabelFrame(win) 
wrapper2 = LabelFrame(win)

mycanvas = Canvas(wrapper1)
mycanvas.pack(side=LEFT, fill="both", expand="yes")

yscrollbar = ttk.Scrollbar(wrapper1, orient="vertical", command=mycanvas.yview)
yscrollbar.pack(side=RIGHT, fill="y")

mycanvas.configure(yscrollcommand=yscrollbar.set)

mycanvas.bind('<Configure', lambda e: mycanvas.configure(scrollregion = mycanvas.bbox('all'))) 


myframe = Frame(mycanvas)
mycanvas.create_window((0,0), window=myframe, anchor="nw")
# myframe.pack() 

wrapper1.pack(fill="both", expand="yes", padx=10, pady=10)
wrapper2.pack(fill="both", expand="yes", padx=10, pady=10)

for i in range(50):
    Button(myframe, text="My Button - "+str(i)).pack()

win.geometry("500x500")
win.resizable(False, False)
win.title("MyScroller")
win.mainloop()
