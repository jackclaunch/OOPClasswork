num1 = ""
num2 = ""
operator = ""


while not type(num1) is int:
    try:
        num1 = int(input('Enter a number: '))
    except ValueError:
        continue

while operator != '+' and operator != '-' and operator != '*' and operator != '/':
    operator = input('Enter a operator: ')

while not type(num2) is int:
    try:
        num2 = int(input('Enter a number: '))
    except ValueError:
        continue


if operator == '+':
    print(num1 + num2)
elif operator == '-':
    print(num1 - num2)
elif operator == '*':
    print(num1 * num2)
elif operator == '/':
    print(num1 / num2)
