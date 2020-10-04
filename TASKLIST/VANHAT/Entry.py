from tkinter import *
root = Tk()
root.geometry('400x200')





def button_command():
    text = entry1.get()
    print(text) 
    #print("test")
    return None

entry1 = Entry(root, width = 20) 
entry1.pack() 

Button(root, text="Button", command=button_command).pack() 


root.mainloop() 