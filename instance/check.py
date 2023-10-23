import sqlite3

conn = sqlite3.connect("spaceUsBase.db")
cur = conn.cursor()


#cur.execute("insert into Users values(2, 'domak', 'scrypt:32768:8:1$0HK722phqU9gSiUZ$a89ae30d455f15df5efb8b3e2edbba5b6dd499267cb8a5058e24c13593e87250526df1d2b892d0c87acc7925821f800a83c8d3ee9d233ba7471e78e376252d6d', 'PostmanRuntime/7.33.0')")
#conn.commit()
users = cur.execute("select * from Users").fetchall()
cur.close()
conn.close()
print(users)
# def check_user():
#     for x in cur.execute("select * from Users").fetchall():
#         print(x)

# def check_post():
#     for x in cur.execute("select * from Posts").fetchall():
#         print(x)

# def main():
#     choose = input("1.users\n2.Posts\n:>");
#     if(int(choose)==1):
#         check_user()
#     elif(int(choose)==2):
#         check_post()
#     else:
#         print("Invalid input option")

# if __name__ == '__main__':
#     main()
#     cur.close()
#     conn.close()
