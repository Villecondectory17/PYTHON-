import taskikanta as tkk 
 
database = r"./pythonsqlite.db"

conn = tkk.create_connection(database) 
sqlite_select_query = """SELECT * FROM Tasks"""
sqlite_delete_query = """DELETE FROM Tasks WHERE tehtava_id = """ 

#tkk.readSqliteTable(conn, sqlite_select_query) 
tkk.deleteRecord(conn, sqlite_delete_query, 5)   