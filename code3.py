import sqlite3
con = sqlite3.connect('Employeedb.db')

cursor = con.cursor()


sqlite_update_query = '''UPDATE Employee
                          SET name = 'Niraj_Patil',
                          phone = 9975840567
                          WHERE empcode = 2;'''
cursor.execute(sqlite_update_query)
sqlite_select_query = '''SELECT * FROM Employee'''
cursor.execute(sqlite_select_query)
record2 = cursor.fetchall()
print(record2)




con.commit()
con.close()