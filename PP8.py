mycourses = {"c_name1": "OOP",
             "c_name2": "Calculus",
             "c_name3": "Old Testament Survey"
             }
courseTotal = 3
while True:
    userInput = input("1. Add a course\n2. Remove a course\n3. Replace a course\n4. Print courses\n5. Exit\n")

    if userInput == "1":
        courseTotal = courseTotal + 1
        mycourses.update({f"c_name{courseTotal}": input("Input the course: ")})

    elif userInput == "2":
        try:
            del mycourses[f"c_name{input("Input the course #: ")}"]
        except KeyError:
            print("The course # does not exist")

    elif userInput == "3":
        mycourses[f"c_name{input("Class # you would like to replace\n")}"] = input("Input the new course: ")

    elif userInput == "4":
        print(mycourses)

    elif userInput == "5":
        break