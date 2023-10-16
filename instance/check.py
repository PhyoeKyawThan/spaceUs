import sqlite3

conn = sqlite3.connect("spaceUsBase.db")
cur = conn.cursor()

users = cur.execute("select * from Users").fetchall()
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