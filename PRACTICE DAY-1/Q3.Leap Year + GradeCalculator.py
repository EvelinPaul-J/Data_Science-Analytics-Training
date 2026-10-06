year = int(input("Enter year:"))
mark = int(input("Enter mark:"))
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print(year, " It is a Leap Year")
else:
    print(year, " It is not a Leap Year")
if mark < 0 or mark > 100:
    print("Invalid marks.Please Enter a value between 0 and 100.")
else:    
    if mark >= 90:
        grade = "O"
    elif mark >= 80:
        grade = "A"
    elif mark >= 70:
        grade = "B"
    elif mark >= 60:
        grade = "C"
    elif mark >= 50:
        grade = "D"
    else:
        grade = "Fail"
    print("Grade:", grade)