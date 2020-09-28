import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """ 
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

#if __name__ == '__main__':
    #create_connection(r"./pythonsqlite.db")

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def readSqliteTable(sqliteConnection, sqlite_select_query): 
    try:
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite") 

        cursor.execute(sqlite_select_query) 
        records = cursor.fetchall()
        print("Total rows are:  ", len(records))
        print("Printing each row") 
        for row in records:
            print(row)
            print("/n") 

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed") 
    return records 

def deleteRecord(sqliteConnection, sqlite_delete_query, record_id): 
    try: 
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        # Poistetaan yksi tietue nyt

        cursor.execute(sqlite_delete_query + str(record_id)) 
        sqliteConnection.commit()
        print("Record deleted successfully ")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to delete record from sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("the sqlite connection is closed")

def main():
    database = r"./pythonsqlite.db"

    sql_create_users_table = """ CREATE TABLE IF NOT EXISTS Users ( 
                                        kayttaja_id integer PRIMARY KEY,
                                        ktunnus text NOT NULL,
                                        salasana text 
                                    ); """ 

    sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS Tasks (
                                    tehtava_id integer PRIMARY KEY,
                                    kayttaja_id text NOT NULL,
                                    tehtava_otsikko text NOT NULL,
                                    tehtava text NOT NULL,
                                    FOREIGN KEY (kayttaja_id) REFERENCES Users (kayttaja_id) 
                                );""" 

    # Luo tietokanta yhteys
    conn = create_connection(database)

    # Luo taulukot
    if conn is not None:
        # create users table
        create_table(conn, sql_create_users_table)

        # Luo tehtävätaulukko
        create_table(conn, sql_create_tasks_table)
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()
