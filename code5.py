import sqlite3
con = sqlite3.connect('Employeedb.db')

cursor = con.cursor()
sqlite_select1_query = '''SELECT * FROM Employee WHERE salary>40000 '''
cursor.execute(sqlite_select1_query)
record3 = cursor.fetchall()
print(record3)




con.commit()
con.close()