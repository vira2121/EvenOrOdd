import sqlite3
con = sqlite3.connect('Employeedb.db')

cursor = con.cursor()

sqlite_count_query = '''SELECT count(*)
                        FROM Employee; '''
cursor.execute(sqlite_count_query)
#sqlite_select_query = '''SELECT * FROM Employee'''
#cursor.execute(sqlite_select_query)
record4 = cursor.fetchall()
print(record4)









con.commit()
con.close()