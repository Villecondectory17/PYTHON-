# Luo tkinter 
import tkinter as tk
import taskikanta as kanta 
from tkinter import *
from tkinter import ttk

# Luo objektit jotka poistaa ja valitsee Taskit
sql_delete_query = """DELETE from Tasks WHERE tehtava_id""" 
sqlite_select_query = """SELECT * FROM Tasks""" 

database = r"./pythonsqlite.db"
user = "ville" 

win = tk.Tk()

# Luo etikettirungot joilla on arvot (win) 
wrapper1 = LabelFrame(win)
wrapper2 = LabelFrame(win)

# Luo Canvas ,joka ottaa parametrinaan wrapper1:sen 
mycanvas = Canvas(wrapper1)
mycanvas.pack(side=LEFT) 

# Luo vierityspalkki jolla on yview menetelmä, komentoasetus canvaasin suhteen.
yscrollbar = ttk.Scrollbar(wrapper1, orient="vertical", command=mycanvas.yview) 
yscrollbar.pack(side=RIGHT, fill="y") 

mycanvas.configure(yscrollcommand=yscrollbar.set) 

mycanvas.bind('<Configure>', lambda e: mycanvas.configure(scrollregion = mycanvas.bbox('all'))) 

# Luo ikkuna jolla on x ja y arvo: 0 ja lisäksi Runko muuttuja jolla on parametrina (Muncanvaasi).
myframe = Frame(mycanvas) 
mycanvas.create_window((0,0), window=myframe, anchor="nw") 

wrapper1.pack(fill="both", expand="yes", padx=10, pady=10)
wrapper2.pack(fill="both", expand="yes", padx=10, pady=10)

# Luo create_connection muuttuja, joka ottaa parametrinaan (tietokannan). 
conn = kanta.create_connection(database) 
sqlite_select_query = """SELECT * FROM Tasks""" 
taskit = kanta.readSqliteTable(conn, sqlite_select_query) 

r = 0 
for tietue in taskit: 
    Button(myframe, width=30, text=tietue[2]).grid(row=r, column=0) 
    Button(myframe, width=6, text="POISTA").grid(row=r, column=1) 
    r = r + 1 

# Luo ikkuna jonka korkeus ja leveys on 500
# Luo Ikkunalle otsikko "MyScroller" 
win.geometry("500x500")
win.resizable(False, False) 
win.title("MyScroller")

win.mainloop() 