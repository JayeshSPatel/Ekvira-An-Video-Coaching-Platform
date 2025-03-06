import sqlite3

con = sqlite3.connect("db.sqlite3")

cur = con.cursor()

for row in cur.execute('select * from auth_user_user_permissions'):
    print(row)

for row in cur.execute('select * from auth_user'):
    print(row)
con.close()