Mark_1 = int(input("Enter the mark 1:"))
Mark_2 = int(input("Enter the mark 2:"))
Mark_3 = int(input("Enter the mark 3:"))
average = (Mark_1 + Mark_2 + Mark_3) / 3
print("Average Percentage is :",average)
if average>=90:
    print("Grade A")
elif average>=75:
    print("Grade B")
elif average>=50:
    print("Grade C")
else:
    print("Fail")