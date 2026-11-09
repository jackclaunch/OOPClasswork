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
Faculty INT PRIMARY KEY,
Name VARCHAR(50),
Department VARCHAR(50),
Courses  TEXT,
)
""")
print("Faculty table created successfully!")
#TODO - modify each so that they work for both faculty table and student table
def insert_student(DBtype):
    sid = int(input("Enter Student ID: "))
    name = input("Enter Name: ")
    dept = input("Enter Department: ")
    courses = []
    while True:
        courses.append(input("Enter Course Name: "))
        addMore = input("Do you want to add more courses? (Y/N): ")
        if addMore == "Y":
            continue
        else:
            break
    courses = json.dumps(courses)
    if DBtype == "StudentMaster":
        gpa = input("Enter GPA: ")
    sql = "INSERT INTO StudentMaster VALUES (%s, %s, %s, %s, %s)"
    values = (sid, name, dept, courses, gpa)
    cursor.execute(sql, values)
    db.commit()
    print("Record inserted successfully!")

def display_students():
    cursor.execute("SELECT * FROM StudentMaster")
    for row in cursor.fetchall():
      print(row)

def update_student():
    sid = int(input("Enter Student ID: "))
    name = input("Enter New Name: ")
    dept = input("Enter New Department: ")
    courses = []
    while True:
        courses.append(input("Enter Course Name: "))
        addMore = input("Do you want to add more courses? (Y/N): ")
        if addMore.upper() == "Y":
            continue
        else:
            break
    courses = json.dumps(courses)
    gpa = input("Enter GPA: ")
    sql = """
    UPDATE Student
    SET Name = %s, Department = %s, Courses = %s, GPA = %s
    WHERE StudentID = %s
    """
    cursor.execute(sql, (name, dept, courses, gpa, sid))
    db.commit()
    print("Record updated!" if cursor.rowcount else "Student not found!")

def delete_student():
    sid = int(input("Enter Student ID: "))
    sql = "DELETE FROM StudentMaster WHERE StudentID = %s"
    cursor.execute(sql, (sid,))
    db.commit()
    print("Record deleted!" if cursor.rowcount else "Student not found!")

while True:
    print("1. Student Table")
    print("2. Faculty Table")
    userView = input("Enter your choice: ")
    if userView == "1":
        modifyType = "StudentMaster"
    elif userView == "2":
        modifyType = "FacultyMaster"
    print("\n1. Insert")
    print("2. Display")
    print("3. Update")
    print("4. Delete")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        insert_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        exit()
    else:
        print("Invalid choice!")
cursor.close()
db.close()
print("Database connection closed.")