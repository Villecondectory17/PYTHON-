#Tuo kaikki tkinteristä 
from tkinter import * 

#Luo ikkuna objekti
window=Tk()

#Määritä neljä tunnistetta Otsikko, tekijä, vuosi, ISBN
l1=Label(window, text="Title") 
l1.grid(row=0,column=0) 

l1=Label(window, text="Author")
l1.grid(row=0,column=2)

l1=Label(window, text="Year")
l1.grid(row=1,column=0)

l1=Label(window, text="ISBN")
l1.grid(row=1,column=2)

#Määritä merkinnät
title_text=StringVar()
e1=Entry(window,textvariable=title_text) 
e1.grid(row=0,column=1)

author_text=StringVar()
e2=Entry(window,textvariable=author_text) 
e2.grid(row=0,column=3)

year_text=StringVar()
e3=Entry(window,textvariable=year_text) 
e3.grid(row=1,column=1)

isbn_text=StringVar()
e4=Entry(window,textvariable=isbn_text) 
e4.grid(row=1,column=3) 

#Määritä listbox
list1=Listbox(window, height=6,width=35)
list1.grid(row=2,column=2,columnspan=2)

#Liitä vierityspalkki luetteloon
sb1=Scrollbar(window) 
window.mainloop()
