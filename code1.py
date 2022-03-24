import sqlite3
con = sqlite3.connect('Employeedb.db')

cursor = con.cursor()
sqlite_insert_query = '''INSERT INTO Employee (empCode,name,phone,email,designation,salary,company_name)
                             VALUES (1,'Viraj',7030841213,'virajadhav2121@gmail.com','BE',38000,'Harman'),
                             (2,'Niraj',7030841114,'nirajpatil21@gmail.com','BE',70000,'SAS'),
                             (3,'Yash',7058305570,'yashraut142@gmail.com','BE',30000,'Capgemini'),
                             (4,'Ankur',9975840852,'ankurmore@gmail.com','BE',50000,'Skillvertex'),
                             (5,'Pratik',9989840852,'pratikgarule12@gmail.com','BSC',25000,'Amdocs')'''
cursor.execute(sqlite_insert_query)
con.commit()
con.close()