import sqlite3

con = sqlite3.connect('Employeedb.db')

curr = con.cursor()
qry = '''CREATE TABLE if not exists Employee(
                  empCode INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT NOT NULL,
                  phone INTEGER NOT NULL UNIQUE,
                  email TEXT NOT NULL UNIQUE,
                  designation TEXT NOT NULL,
                  salary REAL NOT NULL,
                  company_name TEXT NOT NULL)'''
curr.execute(qry)
check=1
while check:
    c = int(input(
        "Main Menu\n1) Add new Record\n2) View all Records \n3) Search specific record by name \n"
        "4) Update specific record \n5) Delete specific record \n"
        "6) Display all details of Employee whose salary is greater than 50000 \n"
        "7) Display the count of total records \n8) All the employees details in alphabetical order, within the specific salary range \n"
        "9) All the employees data, whose salary is less than the average salary of all the employees \n10) Exit\n"))
    if c == 1:
        n = int(input("Enter How Many Record You Enter? "))
        for i in range(n):
            empCode = int(input("Enter Id:"))
            name = (input("Enter Name: "))
            phone = int(input("Enter Phone Number: "))
            email = (input("Enter Address: "))
            designation = (input("Enter Designation: "))
            salary = int(input("Enter the Salary: "))
            company_name = (input("Enter company name: "))
            insert_qry = f"insert into Employee values({empCode},'{name}',{phone},'{email}','{designation}',{salary},'{company_name}')"
            curr.execute(insert_qry)
            con.commit()
    elif c == 2:
        selectqry = "SELECT * FROM Employee"
        curr.execute(selectqry)
        result = curr.fetchall()
        for record in result:
            print(record)
    elif c == 3:
        id1 = input("Enter Name:")
        search_qry = f"SELECT * FROM Employee WHERE name='{id1}' "
        curr.execute(search_qry)
        result1 = curr.fetchall()
        for record in result1:
            print(record)
        con.commit()
    elif c == 4:
        id2 = int(input("Enter Empcode:"))
        addr2 = (input("Enter the updated name: "))
        update_qry = f"update Employee set name='{addr2}' where empCode={id2}"
        curr.execute(update_qry)
        print(curr.rowcount, "Record updated")
        con.commit()
    elif c == 5:
        id3 = int(input("Enter Id:"))
        delt_qry = f"delete from Employee where empCode={id3}"
        curr.execute(delt_qry)
        print(curr.rowcount, "Record deleted")
        con.commit()
    elif c == 6:
        sqlite_select1_query = '''SELECT * FROM Employee WHERE salary>50000 '''
        curr.execute(sqlite_select1_query)
        record3 = curr.fetchall()
        for record in record3:
            print(record)
        con.commit()
    elif c == 7:
        sqlite_count_query = '''SELECT COUNT(*) FROM Employee; '''
        curr.execute(sqlite_count_query)
        record4 = curr.fetchall()
        print(record4)
        con.commit()
    elif c == 8:
        print("All the employees details in alphabetical order, within the specific salary range of 20000 & 60000: ")
        sqlite_display_query = '''SELECT * FROM
        employee
        WHERE
        salary > 20000
        AND
        salary < 60000
        ORDER
        BY
        name; '''
        curr.execute(sqlite_display_query)
        record5 = curr.fetchall()
        for record in record5:
            print(record)
    elif c == 9:
        print("All the employees data, whose salary is less than the average salary of all the employees: ")
        sqlite_display1_query = '''select * from employee where salary < (select avg(salary) from employee); '''
        curr.execute(sqlite_display1_query)
        record6 = curr.fetchall()
        for record in record6:
            print(record)
        con.commit()
    else:
        print("Program Terminated")
        check = 0
    print("ThanKyoU")

