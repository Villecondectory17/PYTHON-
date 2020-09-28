from tkinter import *
import tkinter as tk 
from tkinter import ttk
from tkinter import messagebox
import mysql.connector 


def update(rows): 
    try.delete(*try.get_children())
    for i in rows: 
        try.insert('', 'end', values=i) 

def search():
    q2 = q.get()
    query = "SELECT id, first_name, last_name, age FROM customers WHERE first_name LIKE '%"+q2+"%' OR last_name LIKE '%"+q2+"%'"
    cursor.execute(query)
    rows = cursor.fetchall()
    update(rows) 


def clear():
    query = "SELECT id, first_name, last_name, age FROM customers"
    cursor.execute(query) 
    rows = cursor.fetchall()
    update(rows)

def getrow(event):
    rowid = try.identify_row(event.y) 
    item = try.item(try.focus()) 
    t1.set(item['values'][0])  
    t2.set(item['values'][1])  
    t3.set(item['values'][2]) 
    t4.set(item['values'][3]) 
    #print(item['values'][0])  
    #return True 


def update_customer():
    fname = t2.get()
    lname = t3.get()
    age = t4.get() 
    custid = t1.get()

    if messagebox.askyesno("Confirm Please", "Are You Sure you Want to update this customer?"):  

    #return True

def add_new():
    fname = t2.get()
    lname = t3.get() 
    age = t4.get() 
    query = "INSERT INTO customers(id, first_name, last_name, age, date) VALUES(NULL, %s, %s, %s, NOW())"
    cursor.execute(query, (fname, lname, age)) 
    clear()
    #return True 

def delete_customer():
    customer_id = t1.get() 
    if messagebox.askyesno("Confirm Delete?", "Are you sure you want to delete this customer?"):           
        query = "DELETE FROM customers WHERE id = "+customer_id 
        cursor.execute(query) 
        clear() 
    else:
      return True


mydb = mysql.connector.connect(host="localhost", user="codeworked", passwd="elephant", database="sample", auth_plugin="mysql_native_password")
cursor = mydb.cursor() 


root = Tk() 
q = StringVar() 
t1 = StringVar()
t2 = StringVar()
t3 = StringVar() 
t4 = StringVar() 


warpper1 = LabelFrame(root, text="Customer List")
wrapper2 = LabelFrame(root, text="Search") 
wrapper3 = LabelFrame(root, text="Customer Data")



wrapper1.pack(fill="both", expand="yes", padx=20, pady=10) 
wrapper2.pack(fill="both", expand="yes", padx=20, pady=10) 
wrapper3.pack(fill="both", expand="yes", padx=20, pady=10)

try = ttk.Treeview(wrapper1, columns=(1,2,3,4), show="headings", height="6")
try.pack() 

try.heading(1, text="Customer ID") 
try.heading(2,  text="First Name")
try.heading(3, text="Last Name")
try.heading(4, text="Age") 

try.bind('<Double 1>', getrow)


query = "SELECT id, first_name, last_name, age from customers"
cursor.execute(query) 
rows = cursor.fetchall()
update(rows) 


#Search Section 
lbl = Label(wrapper2, text="Search")
lbl.pack(side=tk.LEFT, padx=10)
ent = Entry(wrapper2, textvariable=q)  
ent.pack(side=tk.LEFT, padx=6) 
btn = Button(wrapper2, text="Search", command=search) 
btn.pack(side=tk.LEFT, padx=6) 
cbtn = Button(wrapper2, text="Clear", command=clear)
cbtn.pack(side=tk.LEFT, padx=6)





#User Data Section 
lbl1 = Label(wrapper3, text="Customer ID")
lbl1.grid(row=0, column=0, padx=5, pady=3)
ent1 = Entry(wrapper3, textvariable=t1) 
ent1.grid(row=0, column=1, padx=5, pady=3)

lbl2 = Label(wrapper3, text="First Name") 
lbl2.grid(row=1, column=0, padx=5, pady=3) 
ent2 = Entry(wrapper3, textvariable=t2)
ent2.grid(row=1, column=1, padx=5, pady=3) 

lbl3 = Label(wrapper3, text="Last Name")
lbl3.grid(row=2, column=0, padx=5, pady=3) 
ent3 = Entry(wrapper3, textvariable=t3)
ent3.grid(row=2, column=1, padx=5, pady=3)

lbl4 = Label(wrapper3, text="Age")
lbl4.grid(row=3, column=0, padx=5, pady=3) 
ent4 = Entry(wrapper3, textvariable=t4)
ent4.grid(row=3, column=1, padx=5, pady=3)

up_btn = Button(wrapper3, text="Update", command=update_customer)  
add_btn = Button(wrapper3, text="Add New", command=add_new)
delete_btn = Button(wrapper3, text="Delete", command=delete_customer) 

add_btn.grid(row=4, column=0, padx=5, pady=3)
up_btn.grid(row=4, column=1, padx=5, pady=3)
delete_btn.grid(row=4, column=2, padx=5, pady=3) 




root.title("My Application")
root.geometry("800x700") 
root.mainloop()


