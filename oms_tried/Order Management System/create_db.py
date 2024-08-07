import sqlite3
def create_db():
    con = sqlite3.connect(database=r'oms.db')
    cur=con.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS company(ID INTEGER PRIMARY KEY AUTOINCREMENT,Name text,GST text,Phone text,Email text,Address text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS product(ID INTEGER PRIMARY KEY AUTOINCREMENT,Name text,Rate text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS orders(ID INTEGER PRIMARY KEY AUTOINCREMENT,Company text,Product text,Quantity text,Status text)")
    con.commit()

create_db()