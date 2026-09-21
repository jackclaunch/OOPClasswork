while True:
    number2 = ""
    print(" 1 Addition\n 2 Subtraction\n 3 Multiplication\n 4 Division\n 5 Exit")
    choice = input("Enter your choice: ")

    if choice == "5":
        exit()

    number1 = ""
    while not type(number1) is int:
        try:
            number1 = int(input('Enter a number: '))
        except ValueError:
            continue

    number2 = ""
    while not type(number2) is int:
        try:
            number2 = int(input('Enter a number: '))
        except ValueError:
            continue

    if choice == "1":
        print(number1 + number2)
    elif choice == "2":
        print(number1 - number2)
    elif choice == "3":
        print(number1 * number2)
    elif choice == "4":
        print(number1 / number2)
    print("")