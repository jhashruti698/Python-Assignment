# Python Database Connection Project which updates any one value in the table and select all the table data and print it.

import mysql.connector as sqlcon

db = sqlcon.connect(host = "localhost", user = "root", passwd = "xyz123", database = "essentials", auth_plugin = 'mysql_native_password')

cur = db.cursor()

cur.execute("update student set marks = 80 where rollno = 102")

cur.execute("select * from student")

for i in cur:
    print(i)


cur.close()
db.commit()