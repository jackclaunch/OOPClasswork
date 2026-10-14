import pickle

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

s1 = Student()
s1.create_new_student()

file1 = open("myStudents.dat", "ab")
pickle.dump(s1, file1)
file1.close()

file2 = open("myStudents.dat", "rb")
while True:
    try:
        data = pickle.load(file2)
        print(data.name)
        print(data.department)
        print(data.id)
    except EOFError:
        break
file2.close()