# Kirjoitetaan tietokantaan uusi rivi
def submit(): 

    conn = sqlite3.connect("tasklist.db")

    c = conn.cursor()

    # Insert into table 

    c.execute("INSERT INTO tasks VALUES (:task)",
        {
            'task' : task.get()
        }
    # commit changes
    conn.commit()

    # close connection 
    conn.close()

    task.delete(0, END) 