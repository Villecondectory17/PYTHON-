from tkinter import *
import sqlite3

root = Tk()
root.title("Tietokanta")
root.geometry("400x400")

# luo tietokanta nimeltä tasklist 
conn = sqlite3.connect("tasklist.db")

c = conn.cursor()

# Poista tietokantataulu nimeltä tasks, jos sellainen on jo olemassa
c.execute("DROP TABLE IF EXISTS tasks")

# luo taulu
sql = '''CREATE TABLE tasks (
    id int,
    task char(20)
)'''
c.execute(sql)

# committa muutokset 
conn.commit()

# sulje tietokantayhteys 
conn.close()

root.mainloop()
