class Student:
    def __init__(self):
        self.id = ""
        self.name = ""
        self.department = ""

    def create_new_student(self):
        self.id = input("Enter student ID: ")
        self.name = input("Enter name: ")
        self.department = input("Enter department: ")

    def display_student(self):
        print("ID:", self.id)
        print("Name:", self.name)
        print("Department:", self.department)

class Faculty:
    def __init__(self):
        self.id = ""
        self.name = ""
        self.role = ""
        self.pay = ""

    def create_new_faculty(self):
        self.id = input("Enter faculty ID: ")
        self.name = input("Enter name: ")
        self.role = input("Enter role: ")
        self.pay = input("Enter pay: ")
    def display_faculty(self):
        print("ID:", self.id)
        print("Name:", self.name)
        print("Role:", self.role)
        print("Pay:", f"${self.pay}")

myFaculty = []
Fac = Faculty()
Fac.create_new_faculty()
Fac.display_faculty()
myFaculty.append(Fac)
Fac = Faculty()
Fac.create_new_faculty()
Fac.display_faculty()
myFaculty.append(Fac)



Stu = Student()
Stu.create_new_student()
Stu.display_student()

