import sqlite3
con = sqlite3.connect('Employeedb.db')

cursor = con.cursor()


sqlite_select_query = '''SELECT * FROM Employee'''
cursor.execute(sqlite_select_query)
records = cursor.fetchall()
print(records)

sqlite_search_query = '''SELECT * FROM Employee WHERE name = 'Viraj' '''
cursor.execute(sqlite_search_query)
record1 = cursor.fetchall()
print(record1)


con.commit()
con.close()