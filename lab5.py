import mysql.connector
import json

# Connect to MySQL (localhost/phpmyadmin5.2.3)
# run wampserver64! may need to install.

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="studentDB"
)
cursor = db.cursor()


cursor.execute("""
    CREATE TABLE IF NOT EXISTS StudentMaster (
        StudentID INT PRIMARY KEY,
        Name VARCHAR(50),
        Department VARCHAR(50),
        Courses TEXT,
        GPA REAL NOT NULL
    )
""")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS FacultyMaster (
        FacultyID INT PRIMARY KEY,
        Name VARCHAR(50),
        Department VARCHAR(50),
        Courses TEXT
    )
""")
db.commit()


def display_items(table):
    cursor.execute(f"SELECT * FROM {table}")
    for row in cursor.fetchall():
        print(row)


def insert_student(sid, name, department, courses, gpa):
    sql = "INSERT INTO StudentMaster VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(sql, (sid, name, department, json.dumps(courses), gpa))
    db.commit()
    return cursor.rowcount


def update_student(sid, name, department, courses, gpa):
    sql = """
        UPDATE StudentMaster
        SET Name = %s, Department = %s, Courses = %s, GPA = %s
        WHERE StudentID = %s
    """
    cursor.execute(sql, (name, department, json.dumps(courses), gpa, sid))
    db.commit()
    return cursor.rowcount


def delete_student(sid):
    cursor.execute("DELETE FROM StudentMaster WHERE StudentID = %s", (sid,))
    db.commit()
    return cursor.rowcount


def insert_faculty(fid, name, department, courses):
    sql = "INSERT INTO FacultyMaster VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (fid, name, department, json.dumps(courses)))
    db.commit()
    return cursor.rowcount


def update_faculty(fid, name, department, courses):
    sql = """
        UPDATE FacultyMaster
        SET Name = %s, Department = %s, Courses = %s
        WHERE FacultyID = %s
    """
    cursor.execute(sql, (name, department, json.dumps(courses), fid))
    db.commit()
    return cursor.rowcount


def delete_faculty(fid):
    cursor.execute("DELETE FROM FacultyMaster WHERE FacultyID = %s", (fid,))
    db.commit()
    return cursor.rowcount


def ask_courses():
    courses = []
    while True:
        courses.append(input("Enter Course Name: "))
        if input("Do you want to add more courses? (Y/N): ").upper() != "Y":
            break
    return courses


class StudentMaster:
    def __init__(self):
        self.sid = ""
        self.name = ""
        self.department = ""
        self.courses = []
        self.gpa = ""

    def get_details(self):
        self.sid = int(input("Enter Student ID: "))
        self.name = input("Enter Student Name: ")
        self.department = input("Enter Department: ")
        self.courses = ask_courses()
        self.gpa = float(input("Enter GPA: "))

    def add_student(self):
        self.get_details()
        insert_student(self.sid, self.name, self.department, self.courses, self.gpa)
        print("Record inserted successfully!")

    def update_student(self):
        self.get_details()
        found = update_student(self.sid, self.name, self.department, self.courses, self.gpa)
        print("Record updated" if found else "Student not found")

    def delete_student(self):
        self.sid = int(input("Enter ID: "))
        found = delete_student(self.sid)
        print("Record deleted" if found else "Student not found")


class FacultyMaster:
    def __init__(self):
        self.fid = ""
        self.name = ""
        self.department = ""
        self.courses = []

    def get_details(self):
        self.fid = int(input("Enter Faculty ID: "))
        self.name = input("Enter Faculty Name: ")
        self.department = input("Enter Department: ")
        self.courses = ask_courses()

    def add_faculty(self):
        self.get_details()
        insert_faculty(self.fid, self.name, self.department, self.courses)
        print("Record inserted successfully")

    def update_faculty(self):
        self.get_details()
        found = update_faculty(self.fid, self.name, self.department, self.courses)
        print("Record updated" if found else "Faculty not found")

    def delete_faculty(self):
        self.fid = int(input("Enter Faculty ID: "))
        found = delete_faculty(self.fid)
        print("Record deleted" if found else "Faculty not found")



while True:
    print("\n1. Student Table")
    print("2. Faculty Table")
    userView = input("Enter your choice: ")
    print("\n1. Insert")
    print("2. Display")
    print("3. Update")
    print("4. Delete")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "5":
        break

    try:
        if userView == "1":
            stu = StudentMaster()
            if choice == "1":
                stu.add_student()
            elif choice == "2":
                display_items("StudentMaster")
            elif choice == "3":
                stu.update_student()
            elif choice == "4":
                stu.delete_student()
            else:
                print("Invalid choice!")
        elif userView == "2":
            fac = FacultyMaster()
            if choice == "1":
                fac.add_faculty()
            elif choice == "2":
                display_items("FacultyMaster")
            elif choice == "3":
                fac.update_faculty()
            elif choice == "4":
                fac.delete_faculty()
            else:
                print("Invalid choice!")
        else:
            print("Invalid choice!")
    except ValueError:
        print("Invalid number entered, try again.")
    except mysql.connector.Error as err:
        print("Database error:", err)


cursor.close()
db.close()
print("Database connection closed.")