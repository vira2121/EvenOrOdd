import sqlite3

def insertData(id,name,marks):
    con = sqlite3.connect('student.db')
    cursor = con.cursor()
    #parametrized query
    insert_query = '''INSERT INTO stud_marks
                         VALUES (?,?,?)'''
    cursor.execute(insert_query,(id, name, marks))
    con.commit()
    con.close()
a = int(input('Enter the student id:'))
b = input('Enter the student name:')
c = int(input('Enter the student marks:'))
insertData(a,b,c)


