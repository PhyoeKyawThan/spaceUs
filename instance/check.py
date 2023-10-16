import sqlite3

conn = sqlite3.connect("spaceUsBase.db")
cur = conn.cursor()

for x in cur.execute("select * from Users").fetchall():
    print(x)
