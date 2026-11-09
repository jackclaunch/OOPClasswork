import mysql.connector
# Connect to MySQL
db = mysql.connector.connect(
host="localhost",
user="root",
password="",
database="studentDB"
)
cursor = db.cursor()

cursor.execute( """
CREATE TABLE IF NOT EXISTS Student (
StudentID INT PRIMARY KEY,
Name VARCHAR(50),
Department VARCHAR(50)
)
""")
print("Student table created successfully!")

def insert_student():
    sid = int(input("Enter Student ID: "))
    name = input("Enter Name: ")
    dept = input("Enter Department: ")
    sql = "INSERT INTO Student VALUES (%s, %s, %s)"
    values = (sid, name, dept)
    cursor.execute(sql, values)
    db.commit()
    print("Record inserted successfully!")

def display_students():
    cursor.execute("SELECT * FROM Student")
    for row in cursor.fetchall():
      print(row)

def update_student():
    sid = int(input("Enter Student ID: "))
    name = input("Enter New Name: ")
    dept = input("Enter New Department: ")
    sql = """
    UPDATE Student
    SET Name = %s, Department = %s
    WHERE StudentID = %s
    """
    cursor.execute(sql, (name, dept, sid))
    db.commit()
    print("Record updated!" if cursor.rowcount else "Student not found!")

def delete_student():
    sid = int(input("Enter Student ID: "))
    sql = "DELETE FROM Student WHERE StudentID = %s"
    cursor.execute(sql, (sid,))
    db.commit()
    print("Record deleted!" if cursor.rowcount else "Student not found!")

while True:
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