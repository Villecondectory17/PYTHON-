from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
#import mysql.connector
import sqlite3

kayttaja_id = "1" 
database = r"./pythonsqlite.db" 

def update(rows):
    trv.delete(*trv.get_children())
    for i in rows:
      trv.insert('', 'end', values=i)

def search():
    q2 = q.get()
    query = "SELECT tehtava_id,luokka, tehtava_otsikko, tehtava FROM Tasks WHERE luokka LIKE ? OR tehtava_otsikko LIKE ? " 
    cursor.execute(query, (q2, q2))
    rows = cursor.fetchall()
    update(rows)


def clear():
    query = "SELECT tehtava_id, luokka, tehtava_otsikko, tehtava FROM Tasks" 
    cursor.execute(query)
    rows = cursor.fetchall()
    update(rows)

def getrow(event):
    rowid = trv.identify_row(event.y)
    item = trv.item(trv.focus())
    t1.set(item['values'][0])
    t2.set(item['values'][1])
    t3.set(item['values'][2])
    t4.set(item['values'][3]) 


def update_task(): 
    tehtava_id = t1.get()
    luokka = t2.get()
    tehtava_otsikko = t3.get()
    tehtava = t4.get() 

    if messagebox.askyesno("Vahvista", "Haluatko varmasti päivittää tehtävän?"): 
        query = "UPDATE Tasks SET luokka = ?, tehtava_otsikko = ?, tehtava = ? WHERE tehtava_id = ?" 
        cursor.execute(query, (luokka, tehtava_otsikko, tehtava, tehtava_id)) 
        mydb.commit()
        clear()
    else:
        return True
    #return True

def add_new():
    luokka = t2.get() 
    tehtava_otsikko = t3.get()
    tehtava = t4.get()
    query = "INSERT INTO Tasks(tehtava_id, kayttaja_id, luokka, tehtava_otsikko, tehtava) VALUES(NULL, ?, ?, ?, ?)"
    cursor.execute(query, (kayttaja_id, luokka, tehtava_otsikko, tehtava))
    mydb.commit()
    clear()
    

def delete_task(): 
    tehtava_id = t1.get()
    if messagebox.askyesno("Vahvista poistaminen?", "Oletko varma että haluat poistaa tehtävän?"):
        query = "DELETE FROM Tasks WHERE tehtava_id = ? "
        cursor.execute(query, (tehtava_id, ))
        mydb.commit() 
        clear()
    else:
      return True

mydb = sqlite3.connect(database)

cursor = mydb.cursor()


root = Tk()
q = StringVar()
t1 = StringVar()
t2 = StringVar()
t3 = StringVar()
t4 = StringVar()

def show_values():
    print (w1.get(), w2.get())
    
wrapper1 = LabelFrame(root, text="Tehtävälista") 
wrapper2 = LabelFrame(root, text="Etsi")
wrapper3 = LabelFrame(root, text="Tehtävän tiedot") 
wrapper31 = Frame(wrapper3)
wrapper32 = Frame(wrapper3) 

master = Tk()
w1 = Scale(master, from_=0, to=42)
w1.set(19)
w1.pack()
w2 = Scale(master, from_=0, to=200, orient=HORIZONTAL)
w2.set(23)
w2.pack()
Button(master, text='Show', command=show_values).pack()  

wrapper1.pack(fill="both", expand="yes", padx=20, pady=10)
wrapper2.pack(fill="both", expand="yes", padx=20, pady=10)
wrapper3.pack(fill="both", expand="yes", padx=20, pady=10)
wrapper31.pack(fill="both", expand="yes", padx=20, pady=10) 
wrapper32.pack(fill="both", expand="yes", padx=20, pady=10) 

trv = ttk.Treeview(wrapper1, columns=(1,2,3,4), show="headings", height="6")

trv.column(1, width=50)
trv.column(2, width=70)
trv.column(3, width=180)
trv.column(4, width=500) 

trv.pack()




trv.heading(1, text="ID") 
trv.heading(2, text="Luokka") 
trv.heading(3, text="Otsikko")
trv.heading(4, text="Tehtävä") 

trv.bind('<Double 1>', getrow)


query = "SELECT tehtava_id, luokka, tehtava_otsikko, tehtava FROM Tasks"  
cursor.execute(query) 
rows = cursor.fetchall()
update(rows)


#Search Section
lbl = Label(wrapper2, text="Hakusana") 
lbl.pack(side=tk.LEFT, padx=10)
ent = Entry(wrapper2, textvariable=q)
ent.pack(side=tk.LEFT, padx=6)
btn = Button(wrapper2, text="Etsi", command=search)
btn.pack(side=tk.LEFT, padx=6)
cbtn = Button(wrapper2, text="Tyhjennä", command=clear) 
cbtn.pack(side=tk.LEFT, padx=6) 





#User Data Section
lbl1 = Label(wrapper31, text="ID") 
lbl1.grid(row=0, column=0, padx=5, pady=3)
ent1 = Entry(wrapper31, textvariable=t1, width=5) 
ent1.grid(row=0, column=1, padx=5, pady=3, sticky=W) 

lbl2 = Label(wrapper31, text="Luokka")
lbl2.grid(row=1, column=0, padx=5, pady=3)
ent2 = Entry(wrapper31, textvariable=t2, width=7)
ent2.grid(row=1, column=1, padx=5, pady=3, sticky=W) 

lbl3 = Label(wrapper31, text="Otsikko")
lbl3.grid(row=2, column=0, padx=5, pady=3)
ent3 = Entry(wrapper31, textvariable=t3, width=18)
ent3.grid(row=2, column=1, padx=5, pady=3, sticky=W) 

lbl4 = Label(wrapper31, text="Tehtävä") 
lbl4.grid(row=3, column=0, padx=5, pady=3)
ent4 = Entry(wrapper31, textvariable=t4, width=50)
ent4.grid(row=3, column=1, padx=5, pady=3, sticky=W)  

up_btn = Button(wrapper32, text="Päivitä", command=update_task) 
add_btn = Button(wrapper32, text="Lisää uusi", command=add_new) 
delete_btn = Button(wrapper32, text="Poista", command=delete_task)  

add_btn.grid(row=4, column=0, padx=5, pady=3)
up_btn.grid(row=4, column=1, padx=5, pady=3)
delete_btn.grid(row=4, column=2, padx=5, pady=3)




root.title("My Application")
root.geometry("800x700")
root.mainloop() 
