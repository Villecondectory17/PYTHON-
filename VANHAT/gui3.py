from tkinter import *
import os 

def delete2():
    screen3.destroy()

def delete3():
    screen4.destroy()

def delete4():
    screen5.destroy()

def logout():
    screen7.destroy()

def saved():
    screen10 = Toplevel(screen)
    screen10.title("Saved") 
    screen10.geometry("100x100") 
    Label(screen10, text = "Saved").pack() 

def save():

    filename = raw_filename.get()
    notes = raw_notes.get() 

    data = open(filename, "w")
    data.write(notes)
    data.close()

    saved() 

    #print("saved") 

def create_notes():
    global raw_filename 
    raw_filename = StringVar() 
    global raw_notes 
    raw_notes = StringVar()

    screen9 = Toplevel(screen)
    screen9.title("Info") 
    screen9.geometry("300x250") 
    Label(screen9, text = "Please enter a filename for the note below : ").pack()
    Entry(screen9, textvariable = raw_filename).pack() 
    Label(screen9, text = "Please enter the notes for the file below : ").pack() 
    Entry(screen9, textvariable = raw_notes).pack() 
    Button(screen9, text = "Save", command = save).pack() 

def view_notes1(): 
    filename1 = raw_filename1.get()
    data = open(filename1, "r") 
    data1 = data.read() 
    screen12 = Toplevel(screen) 
    screen12.title("Notes") 
    screen12.geometry("400x400")
    Label(screen12, text = data1).pack() 
    #Label(screen12, text = all_files).pack() 
    #data.close() 


def view_notes():
    screen11 = Toplevel(screen) 
    screen11.title("Info") 
    screen11.geometry("250x250") 
    all_files = os.listdir()
    Label(screen11, text = "Please use one of the filenames below").pack() 
    Label(screen11, text = all_files).pack()
    global raw_filename1 
    raw_filename1 = StringVar() 
    Entry(screen11, textvariable=raw_filename1).pack() 
    Button(screen11, command=view_notes1, text = "OK").pack()

    #Label(screen9, text = "Welcome to the dashboard").pack()


def session():
    screen8 = Toplevel(screen)
    screen8.title("dashboard")
    screen8.geometry("400x400")
    Label(screen8, text = "Welcome to the dashboard").pack()
    Button(screen8, text = "Create Note", command = create_notes).pack() 
    Button(screen8, text = "View Note", command = view_notes).pack() 
    Button(screen8, text = "Delete Note").pack() 

def login_sucess():
    session()

def password_not_recognised():
    global screen4 
    screen4.title("Success")
    screen4.geometry("150x100")
    Label(screen4, text = "Password Error").pack()
    Button(screen4, text = "OK", command =delete3).pack()

def user_not_found():
    global screen5 
    screen5 = Toplevel(screen)
    screen5.title("Success")
    screen5.geometry("150x100")
    Label(screen5, text = "User Not Found").pack()
    Button(screen5, text = "OK", command =delete4).pack()

def register_user():
    print("Working")
    global username_info
    username_info = username.get()
    password_info = password.get()

    file=open(username_info, "w")
    file.write(username_info+"\n")
    file.write(password_info)
    file.close() 

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(screen1, text = "Registration Sucess", fg = "green" ,font = ("calibri", 11)).pack()

def login_verify():
    global username1
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

    list_of_files 
