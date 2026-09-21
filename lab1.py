while True:

    pickNum = input("1. Area of a rectangle\n2. Volume of a cube\n"
                        "3. Area of a circle\n4. Circumference of a circle\n5. Exit\n")
    if pickNum == "5":
        break

    if pickNum == "1" or pickNum == "2":
        length = int(input("Enter the length of the rectangle: "))
        width = int(input("Enter the width of the rectangle: "))
        if pickNum == "2":
            height = int(input("Enter the height of the rectangle: "))
            print(f"The volume of the rectangular cube is {length * width * height}")
        else:
            print(f"The area of the rectangle is {length*width}")
    elif pickNum == "3" or pickNum == "4":
        radius = int(input("Enter the radius of the circle: "))
        if pickNum == "3":
            print(f"The area of the circle is {3.14 * radius * radius}")
        else:
            print(f"The circumference of the circle is {3.14 * radius * 2}")
    print("")