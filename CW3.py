class Student:
    def __init__(self):
        self.id = ""
        self.name = ""
        self.advisor = ""

    def create_new_student(self):
        self.id = int(input("Enter student ID: "))
        self.name = input("Enter name: ")

    def display_student(self):
        print("ID:", self.id)
        print("Name:", self.name)

    def assign_advisor(self, faculty_id):
        self.advisor = faculty_id

class Faculty:
    def __init__(self):
        self.id = ""
        self.name = ""
        self.students_enrolled = []

    def create_new_faculty(self):
        self.id = int(input("Enter faculty ID: "))
        self.name = input("Enter name: ")
    def display_faculty(self):
        print("ID:", self.id)
        print("Name:", self.name)
    def enroll_student(self, student_id):
        self.students_enrolled.append(student_id)

class Course:
    def __init__(self):
        self.id = ""
        self.name = ""
        self.professor = ""
        self.students = []
    def create_new_course(self):
        self.id = int(input("Enter course ID: "))
        self.name = input("Enter name: ")
    def display_course(self):
        print("ID:", self.id)
        print("Name:", self.name)
    def add_prof(self, prof_id):
        self.professor = prof_id
    def add_student(self, student_ID):
        self.students.append(student_ID)

myStudentsList = []
myFaculty = []
myCourses = []


for i in range(int(input("How many faculty members?"))):
    Fac = Faculty()
    Fac.create_new_faculty()
    Fac.display_faculty()
    myFaculty.append(Fac)

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
        studentID = int(input("Enter student ID: "))
        facultyID = int(input("Enter faculty ID: "))
        for i in range(len(myStudentsList)):
            try:
                Stu = myStudentsList[i]
                if Stu.id == studentID:
                    for j in range(len(myFaculty)):
                        try:
                            Fac = myFaculty[j]
                            if Fac.id == facultyID:
                                Stu.assign_advisor(facultyID)
                        except IndexError:
                            print("Invalid Faculty ID")
            except IndexError:
                print("Invalid Student ID")

    elif userInput == "2":
        if userInput == "1":
            studentID = int(input("Enter student ID: "))
            facultyID = int(input("Enter faculty ID: "))
            for i in range(len(myFaculty)):
                try:
                    Fac = myFaculty[i]
                    if Fac.id == facultyID:
                        for j in range(len(myStudentsList)):
                            try:
                                Stu = myStudentsList[j]
                                if Stu.id == studentID:
                                    Fac.enroll_student(studentID)
                            except IndexError:
                                print("Invalid Faculty ID")
                except IndexError:
                    print("Invalid Student ID")

    elif userInput == "3":
        facultyID = int(input("Enter faculty ID: "))
        courseID = int(input("Enter course ID: "))
        for i in range(len(myCourses)):
            try:
                course = myCourses[i]
                if course.id == courseID:
                    for j in range(len(myFaculty)):
                        try:
                            Fac = myFaculty[j]
                            if Fac.id == facultyID:
                                Course.add_prof(facultyID)
                        except IndexError:
                            print("Invalid Faculty ID")
            except IndexError:
                print("Invalid Course ID")

    elif userInput == "4":
        courseID = int(input("Enter course ID: "))
        studentID = int(input("Enter student ID: "))
        for i in range(len(myCourses)):
            try:
                course = myCourses[i]
                if course.id == courseID:
                    for j in range(len(myStudentsList)):
                        try:
                            Stu = myStudentsList[j]
                            if Stu.id == studentID:
                                Course.add_student(studentID)
                        except IndexError:
                            print("Invalid Student ID")
            except IndexError:
                print("Invalid Course ID")