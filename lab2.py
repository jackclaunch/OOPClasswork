myEmployees = {
    "e1": {
        "name": "Jim",
        "basic pay": 80000,
        "allowance": 15000,
        "deductions": 1300,
        "taxes": 2500,
        "gross pay": "",
        "net pay": ""
    },
    "e2": {
        "name": "Jack",
        "basic pay": 65000,
        "allowance": 10000,
        "deductions": 900,
        "taxes": 1800,
        "gross pay": "",
        "net pay": ""
    },
    "e3": {
        "name": "George",
        "basic pay": 72000,
        "allowance": 12000,
        "deductions": 1100,
        "taxes": 2100,
        "gross pay": "",
        "net pay": ""
    },
    "e4": {
        "name": "Angela",
        "basic pay": 58000,
        "allowance": 8000,
        "deductions": 700,
        "taxes": 1500,
        "gross pay": "",
        "net pay": ""
    },
    "e5": {
        "name": "Kevin",
        "basic pay": 60000,
        "allowance": 9000,
        "deductions": 800,
        "taxes": 1600,
        "gross pay": "",
        "net pay": ""
                 }
            }

def checkPay(employee):
    employee["gross pay"] = employee["basic pay"] + employee["allowance"]
    employee["net pay"] = employee["gross pay"] - employee["deductions"] - employee["taxes"]
    return employee

for employeeID, employeeInfo in myEmployees.items():
    checkPay(employeeInfo)

def addEmployee(idNum):
    myEmployees.update({
                    f"e{idNum}":
                                 {"name": input("Enter name: "),
                                  "basic pay": int(input("Enter basic pay: ")),
                                  "allowance": int(input("Enter allowance: ")),
                                  "deductions": int(input("Enter deductions: ")),
                                  "taxes": int(input("Enter taxes: ")),
                                  "gross pay": "",
                                  "net pay": ""
                                  }
                             })
    checkPay(myEmployees[f"e{idNum}"])

def delEmployee():
    idInput = input("ID of employee to delete: ")
    del myEmployees[f"e{idInput}"]

def modifyEmployee():
        idInput = input("ID of employee to modify: ")
        userEditInput = input("1. edit basic pay\n2. edit allowance\n3. edit deductions\n4. edit taxes")
        editInput = {
                        "1": "basic pay",
                        "2": "allowance",
                        "3": "deductions",
                        "4": "taxes"
                        }
        newValType = editInput[userEditInput]
        newVal = int(input(f"Edit {newValType} to: "))
        myEmployees[f"e{idInput}"][newValType] = newVal
        checkPay(myEmployees[f"e{idInput}"])

def printEmployees():
    userInput = input("1. Print all employees\n2. Print specific employee\n")
    if userInput == "1":
        for employeeInfo in myEmployees.items():
            print(employeeInfo)
    elif userInput == "2":
        idInput = input("ID of employee to print: ")
        print(myEmployees[f"e{idInput}"])

id = 5
while True:
    userInput = input("1. Add an employee \n2. Remove an employee\n"
                      "3. Modify an employee\n4. Print employees\n5. Exit\n")
    
    if userInput == "1":
        id = id + 1
        addEmployee(id)
    elif userInput == "2":
        delEmployee()
    elif userInput == "3":
        modifyEmployee()
    elif userInput == "4":
        printEmployees()
    elif userInput == "5":
        break
    print("\n\n")