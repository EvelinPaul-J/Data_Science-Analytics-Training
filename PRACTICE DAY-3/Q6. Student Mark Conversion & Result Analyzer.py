students = int(input("Students: "))
print("Student\tTotal\tAverage\tGrade")
for i in range(students):
    name = input("Name: ")
    marks = input("Marks: ").split()
    valid = True
    numbers = []
    for mark in marks:
        try:
            value = int(mark)
            if value < 0 or value > 100:
                valid = False
            numbers.append(value)
        except ValueError:
            valid = False
    if valid and len(numbers) > 0:
        total = sum(numbers)
        average = total / len(numbers)
        if average >= 90:
            grade = "A+"
        elif average >= 80:
            grade = "A"
        elif average >= 70:
            grade = "B"
        elif average >= 60:
            grade = "C"
        elif average >= 50:
            grade = "D"
        else:
            grade = "F"
        print(name, "\t", total, "\t", format(average, ".2f"), "\t", grade)
    else:
        print(name, "\tInvalid marks")