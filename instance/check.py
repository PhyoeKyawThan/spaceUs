import sqlite3

conn = sqlite3.connect("spaceUsBase.db")
cur = conn.cursor()


#cur.execute("insert into Users values(2, 'domak', 'scrypt:32768:8:1$0HK722phqU9gSiUZ$a89ae30d455f15df5efb8b3e2edbba5b6dd499267cb8a5058e24c13593e87250526df1d2b892d0c87acc7925821f800a83c8d3ee9d233ba7471e78e376252d6d', 'PostmanRuntime/7.33.0')")
#conn.commit()
#users = cur.execute("select Posts.user_id, Posts.post_id, Actions.love from Posts, Actions where Posts.id=Actions.post_id").fetchall()
#users = cur.execute("select * from Actions where post_id = '7a11479f-1d94-4fa4-bf79-f60c79705e52'").fetchall()

options = """
1.Users\n
2.Posts\n
3.Actions\n
4.Raw
"""
print(options)
quest = 5
while quest != 0:
    quest = int(input(":> "))
    if quest == 1:
        print(cur.execute("select * from Users").fetchall())
    elif quest == 2:
        print(cur.execute("select * from Posts").fetchall())
    elif quest == 3:
        print(cur.execute("select * from Actions").fetchall())
    elif quest == 4:
        raw = input("(RAW):> ")
        print(cur.execute(f"{raw}").fetchall())
    else: 
        continue
    

        