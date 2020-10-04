
def delete(): 

    conn = sqlite3.connect("tasklist.db")

    c = conn.cursor()

    c.execute("DELETE FROM tasks WHERE oid=" + delete_box.get())
        
    delete_box.delete(0, END)

    # commit changes
    conn.commit()

    # close connection 
    conn.close()

