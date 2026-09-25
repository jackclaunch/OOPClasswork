myStack = []

def push(item):
    myStack.append(item)

def pop():
    myStack.pop()

def display():
    print(myStack)

while True:
    userInput = input("1. Push\n2. Pop\n3. Display\n4. Exit\n")

    if userInput == "1":
        push(input("Value: "))
    elif userInput == "2":
        pop()
        print("Dequeuing...")
    elif userInput == "3":
        display()
    elif userInput == "4":
        break
    print("")