import mysql.connector
import json
# Connect to MySQL (localhost/phpmyadmin5.2.3)
#run wampserver64! may need to install.

db = mysql.connector.connect(
host="localhost",
user="root",
password="",
database="studentDB"
)
cursor = db.cursor()
#TODO- make classes for studentMaster and FacultyMaster
cursor.execute( """
CREATE TABLE IF NOT EXISTS StudentMaster (
StudentID INT PRIMARY KEY,
Name VARCHAR(50),
Department VARCHAR(50),
Courses  TEXT,
GPA REAL NOT NULL
)
""")
print("Student table created successfully!")

cursor.execute( """
CREATE TABLE IF NOT EXISTS FacultyMaster (
FacultyID INT PRIMARY KEY,
Name VARCHAR(50),
Department VARCHAR(50),
Courses  TEXT
)
""")
print("Faculty table created successfully!")

def display_items(DBtype):
    cursor.execute(f"SELECT * FROM {DBtype}")
    for row in cursor.fetchall():
      print(row)

class StudentMaster:
    def __init__(self):
        self.sid = ""
        self.name = ""
        self.department = ""
        self.courses = []
        self.gpa = ""

    def add_student(self):
        self.sid = input("Enter Student ID: ")
        self.name = input("Enter Student Name: ")
        self.department = input("Enter Department: ")
        while True:
            self.courses.append(input("Enter Course Name: "))
            addMore = input("Do you want to add more courses? (Y/N): ")
            if addMore.upper() == "Y":
                continue
            else:
                break
        self.courses = json.dumps(self.courses)
        self.gpa = input("Enter GPA: ")
        sql = "INSERT INTO StudentMaster VALUES (%s, %s, %s, %s, %s)"
        values = (self.sid, self.name, self.department, self.courses, self.gpa)
        cursor.execute(sql, values)
        db.commit()
        print("Record inserted successfully!")

    def update_student(self):
        self.sid = int(input("Enter Student ID: "))
        self.name = input("Enter Student Name: ")
        self.department = input("Enter Department: ")
        while True:
            self.courses.append(input("Enter Course Name: "))
            addMore = input("Do you want to add more courses? (Y/N): ")
            if addMore.upper() == "Y":
                continue
            else:
                break
        self.courses = json.dumps(self.courses)
        self.gpa = input("Enter GPA: ")
        sql = """
                UPDATE Student
                SET Name = %s, Department = %s, Courses = %s, GPA = %s
                WHERE StudentID = %s
                """
        cursor.execute(sql, (self.name, self.department, self.courses, self.gpa, self.sid))
        db.commit()
        print("Record updated!" if cursor.rowcount else "Student not found!")

    def delete_student(self):
        self.sid = int(input("Enter ID: "))
        sql = "DELETE FROM StudentMaster WHERE StudentID = %s"
        cursor.execute(sql, (self.sid,))
        db.commit()
        print("Record deleted!" if cursor.rowcount else "Student not found!")


class FacultyMaster:
    def __init__(self):
        self.sid = ""
        self.name = ""
        self.department = ""
        self.courses = []

    def add_faculty(self):
        self.sid = int(input("Enter Faculty ID: "))
        self.name = input("Enter Faculty Name: ")
        self.department = input("Enter Department: ")
        while True:
            self.courses.append(input("Enter Course Name: "))
            addMore = input("Do you want to add more courses? (Y/N): ")
            if addMore.upper() == "Y":
                continue
            else:
                break
        self.courses = json.dumps(self.courses)

        sql = "INSERT INTO FacultyMaster VALUES (%s, %s, %s, %s)"
        values = (self.sid, self.name, self.department, self.courses)
        cursor.execute(sql, values)
        db.commit()
        print("Record inserted successfully!")

    def update_faculty(self):
        self.sid = int(input("Enter Faculty ID: "))
        self.name = input("Enter Faculty Name: ")
        self.department = input("Enter Department: ")
        while True:
            self.courses.append(input("Enter Course Name: "))
            addMore = input("Do you want to add more courses? (Y/N): ")
            if addMore.upper() == "Y":
                continue
            else:
                break
        self.courses = json.dumps(self.courses)
        sql = """
                UPDATE Faculty
                SET Name = %s, Department = %s, Courses = %s
                WHERE FacultyID = %s
                """
        cursor.execute(sql, (self.name, self.department, self.courses, self.sid))
        db.commit()
        print("Record updated!" if cursor.rowcount else "Faculty not found!")

    def delete_faculty(self):
        self.sid = int(input("Enter Faculty ID: "))
        sql = "DELETE FROM FacultyMaster WHERE FacultyID = %s"
        cursor.execute(sql, (self.sid,))
        db.commit()
        print("Record deleted!" if cursor.rowcount else "Faculty not found!")



while True:
    print("1. Student Table")
    print("2. Faculty Table")
    userView = input("Enter your choice: ")
    print("\n1. Insert")
    print("2. Display")
    print("3. Update")
    print("4. Delete")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if userView == "1":
        if choice == "1":
            stu = StudentMaster()
            stu.add_student()
        elif choice == "2":
            display_items("StudentMaster")
        elif choice == "3":
            stu = StudentMaster()
            stu.update_student()
        elif choice == "4":
            stu = StudentMaster()
            stu.delete_student()
        elif choice == "5":
            break
    elif userView == "2":
        if choice == "1":
            fac = FacultyMaster()
            fac.add_faculty()
        elif choice == "2":
            display_items("FacultyMaster")
        elif choice == "3":
            fac = FacultyMaster()
            fac.update_faculty()
        elif choice == "4":
            fac = FacultyMaster()
            fac.delete_faculty()
        elif choice == "5":
            break


"""    
    print("\n1. Insert")
    print("2. Display")
    print("3. Update")
    print("4. Delete")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        insert_item(modifyType)
    elif choice == "2":
        display_items(modifyType)
    elif choice == "3":
        update_item(modifyType)
    elif choice == "4":
        delete_item(modifyType)
    elif choice == "5":
        exit()
    else:
        print("Invalid choice!")
"""
cursor.close()
db.close()
print("Database connection closed.")