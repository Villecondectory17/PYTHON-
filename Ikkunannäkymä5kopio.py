# Päivitä yksittäistä tehtävää, kutsutaan funktiosta edit 
def update():
    conn = sqlite3.connect("tasklist.db")

    c = conn.cursor()
    record_id = delete_box.get()

    c.execute("""UPDATE tasks SET
        task = :task

        WHERE oid = :oid""",
        {
            'task': task_editor.get(),
            'oid': record_id
        })

    conn.commit()
    conn.close()
    editor.destroy()

# Editointi-ikkuna tehtävän muiokkaamiseen. Kutsuu funktiota update().
def edit():
    global editor
    editor = Tk()
    editor.title("Päivitä")
    editor.geometry("400x400")

    conn = sqlite3.connect("tasklist.db")

    c = conn.cursor()

    record_id = delete_box.get()
    c.execute("SELECT * FROM tasks WHERE oid = " + record_id)
    records=c.fetchall()

    global task_editor

    task_label = Label(editor, text="Tehtävä")
    task_label.grid(row=0, column=0, pady=(10,0))

    task_editor = Entry(editor, width=30)
    task_editor.grid(row=0, column=1, padx=20, pady=(10,0))

    for record in records:
        task_editor.insert(0, record[0])

    save_btn = Button(editor, text="Tallenna", command=update)
    save_btn.grid(row=2, column=0, columnspan=2, pady=10, padx=10)

    