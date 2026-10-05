class Student:
    def __init__(self):
        self.id = ""
        self.name = ""
        self.department = ""
        self.advisor = ""

    def create_new_student(self):
        self.id = int(input("Enter student ID: "))
        self.name = input("Enter name: ")
        self.department = input("Enter department: ")

    def display_student(self):
        print("ID:", self.id)
        print("Name:", self.name)
        print("Department:", self.department)

    def assign_advisor(self, faculty_id):
        self.advisor = faculty_id

class Faculty:
    def __init__(self):
        self.id = ""
        self.name = ""
        self.role = ""
        self.pay = ""

    def create_new_faculty(self):
        self.id = int(input("Enter faculty ID: "))
        self.name = input("Enter name: ")
        self.role = input("Enter role: ")
        self.pay = input("Enter pay: ")
    def display_faculty(self):
        print("ID:", self.id)
        print("Name:", self.name)
        print("Role:", self.role)
        print("Pay:", f"${self.pay}")

class Course:
    def __init__(self):
        self.id = ""
        self.name = ""
    def create_new_course(self):
        self.id = int(input("Enter course ID: "))
        self.name = input("Enter name: ")
    def display_course(self):
        print("ID:", self.id)
        print("Name:", self.name)

myStudentsList = []
myFaculty = []
myCourses = []


for i in range(int(input("How many faculty members?"))):
    Fac = Faculty()
    Fac.create_new_faculty()
    Fac.display_faculty()
    myFaculty.append(Fac)

    #Fac = myFaculty[0]
    #Fac.display_faculty()

for i in range(int(input("How many students?"))):
    Stu = Student()
    Stu.create_new_student()
    Stu.display_student()
    myStudentsList.append(Stu)

for i in range(int(input("How many courses?"))):
    Course = Course()
    Course.create_new_course()
    Course.display_course()
    myCourses.append(Course)

while True:
    userInput = input("1. Assign advisors\n2. Enroll students\n3. Add teacher to course\n4. Enroll student to course")
    if userInput == "1":
        facultyID = int(input("Enter faculty ID: "))
        for i in range(len(myFaculty)):
            try:
                Fac = myFaculty[i]
                if Fac.id == facultyID:
                    Stu.assign_advisor(facultyID)
            except IndexError:
                print("Invalid ID")
