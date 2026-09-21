students = {"s1":
                {"name": "Jim",
                 "major": "CS",
                 "year": "Freshman",
                 "gpa": "3.8"
                 },
            "s2":
                {"name": "Jack",
                 "major": "CS",
                 "year": "Freshman",
                 "gpa": "3.8"
                 }
            }
i = 2
while True:
    userInput = input("1. Add a student\n2. Remove a student\n"
                      "3. Edit a student\n4. Print students\n5. Exit\n")
    if userInput == "1":
        i = i + 1
        students.update(
            {
                f"s{i}":
                             {"name": input("Enter name: "),
                              "major": input("Enter major: "),
                              "year": input("Enter year: "),
                              "gpa": input("Enter gpa: ")
                              }
                         }
                        )
    elif userInput == "2":
        del students[f"s{input("Student # you would like to delete: ")}"]

    elif userInput == "3":
        editStudent = input("Which student # would you like to edit?\n")
        userEditInput = input("1. edit name\n2. edit major\n3. edit year\n4. edit gpa\n")

        editInput = {"1": "name",
                     "2": "major",
                     "3": "year",
                     "4": "gpa"}

        students["s"+ editStudent][editInput[userEditInput]] = input("new " + editInput[userEditInput] + ": ")


    elif userInput == "4":
        print(students)
    elif userInput == "5":
        break