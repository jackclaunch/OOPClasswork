student_dict = {}
i = 0

def add_student(student_id):
    student_name = input("Enter student name: ")
    lab1 = int(input("Enter lab 1 grade: "))
    lab2 = int(input("Enter lab 2 grade: "))
    lab3 = int(input("Enter lab 3 grade: "))
    lab4 = int(input("Enter lab 4 grade: "))
    lab5 = int(input("Enter lab 5 grade: "))
    total = lab1 + lab2 + lab3 + lab4 + lab5


    student_dict.update({f"Student{student_id}": {
    "Name": student_name,
    "Lab1": lab1,
    "Lab2": lab2,
    "Lab3": lab3,
    "Lab4": lab4,
    "Lab5": lab5,
    "Total": total,
    "Percent": (int(total)/50) * 100,
    "Average": total/5
    }
})

while True:
    userInput = input("1. Add a student\n2. Delete a student\n"
                      "3. Print all students\n4. Print one student\n5. Exit\n")
    if userInput == "1":
        add_student(i)
        i = i + 1
    elif userInput == "2":
        del student_dict[input("Enter student ID")]
    elif userInput == "3":
        print(student_dict)
    elif userInput == "4":
        print(student_dict[f"Student{input("Student ID:")}"])
    elif userInput == "5":
        break