import MySQLdb as mysql

conn = mysql.connect(
    host='localhost',
    database='emp',
    user='root',
    password='')

cursor = conn.cursor()
cursor.execute("select * from emp")
data = cursor.fetchall()

for x in data:
    print(x[1])
