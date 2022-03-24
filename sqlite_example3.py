import sqlite3

def insertMultipleData(DataList):
    con = sqlite3.connect('student.db')
    cursor = con.cursor()
    #parametrized query
    insert_query = '''INSERT INTO stud_marks
                         VALUES (?,?,?)'''
    cursor.executemany(insert_query,DataList)
    con.commit()

    print('Total records inserted: ',cursor.rowcount)
    con.commit()
    con.close()

DataList = [(6,'Viraj',92),(7,'Anny',97),(8,'Samuel',95)]
insertMultipleData(DataList)

