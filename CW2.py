mainList = []

def checkint(num):
    try:
        num = int(num)
        return num
    except ValueError:
        return False

while True:
    userInput = input("1. Add an element to the list\n2. Remove an element from the list\n"
                      "3. Replace an element in the list\n4. Sort the elements in the list\n"
                      "5. Print the list\n6. Exit\n")

    if userInput == "6":
        break

    elif userInput == "1":
        userAppend = input("Input the element: ")
        userAppend = checkint(userAppend)
        if userAppend == False:
            print("Insert a number")
            continue
        mainList.append(userAppend)

    elif userInput == "2":
        userRemove = input("Input the element to be removed: ")
        userRemove = checkint(userRemove)
        if userRemove == False:
            print("Insert a number")
            continue
        try:
            mainList.remove(userRemove)
        except ValueError:
            print("Element not in the list")

    elif userInput == "3":
        if not mainList:
            print("The list is empty, nothing to replace")
            continue

        userReplaceThis = input("Input the element to be replaced: ")
        userReplaceThis = checkint(userReplaceThis)
        if userReplaceThis == False:
            print("Insert a number")
            continue

        try:
            index = mainList.index(userReplaceThis)
        except ValueError:
            print("Element not in the list\n")
            continue

        userNewVal = input("Input the new value: ")
        userNewVal = checkint(userNewVal)
        if userNewVal == False:
            print("Insert a number")
            continue
        mainList[index] = userNewVal

    elif userInput == "4":
        print("Sorting...")
        mainList.sort()

    elif userInput == "5":
        print(mainList)
    print("")

