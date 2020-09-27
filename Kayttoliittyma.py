import tkinter as tk
import taskikanta as kanta 
from tkinter import *
from tkinter import ttk

sql_delete_query = """DELETE from Tasks WHERE tehtava_id""" 
sqlite_select_query = """SELECT * FROM Tasks""" 

database = r"./pythonsqlite.db"
user = "ville" 

win = tk.Tk()

wrapper1 = LabelFrame(win)
wrapper2 = LabelFrame(win)

mycanvas = Canvas(wrapper1)
mycanvas.pack(side=LEFT) 

yscrollbar = ttk.Scrollbar(wrapper1, orient="vertical", command=mycanvas.yview) 
yscrollbar.pack(side=RIGHT, fill="y") 

mycanvas.configure(yscrollcommand=yscrollbar.set) 

mycanvas.bind('<Configure>', lambda e: mycanvas.configure(scrollregion = mycanvas.bbox('all'))) 

myframe = Frame(mycanvas) 
mycanvas.create_window((0,0), window=myframe, anchor="nw") 

wrapper1.pack(fill="both", expand="yes", padx=10, pady=10)
wrapper2.pack(fill="both", expand="yes", padx=10, pady=10)

conn = kanta.create_connection(database) 
sqlite_select_query = """SELECT * FROM Tasks""" 
taskit = kanta.readSqliteTable(conn, sqlite_select_query) 

r = 0 
for tietue in taskit: 
    Button(myframe, width=30, text=tietue[2]).grid(row=r, column=0) 
    Button(myframe, width=6, text="POISTA").grid(row=r, column=1) 
    r = r + 1 

win.geometry("500x500")
win.resizable(False, False) 
win.title("MyScroller")



win.mainloop()

