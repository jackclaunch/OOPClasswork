studentName = input('Enter student name: ')

grade1 = int(input('Enter grade: '))
grade2 = int(input('Enter grade: '))
grade3 = int(input('Enter grade: '))

totalGrade = (grade1 + grade2 + grade3) / 3
totalGrade = round(totalGrade)

if totalGrade > 90:
    print(f"{studentName} got an A with a grade of {totalGrade}")
elif 90 > totalGrade > 80:
    print(f"{studentName} got a B with a grade of {totalGrade}")
elif 80 > totalGrade > 70:
    print(f"{studentName} got a C with a grade of {totalGrade}")
elif 70 > totalGrade > 60:
    print(f"{studentName} got a D with a grade of {totalGrade}")
else:
    print(f"{studentName} got a F with a grade of {totalGrade}")