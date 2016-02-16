import sqlite3 as sql
def insert_account_holder(username,password,homefolder,grantsudo,shelltype):
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO account_holder (username,password,homefolder,grantsudo,shelltype) VALUES (?,?,?,?,?)", (username,password,homefolder,grantsudo,shelltype) )
        con.commit()
