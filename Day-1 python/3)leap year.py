year = int(input("Enter a year: "))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("It is a Leap Year")
else:
    print("Not a Leap Year")