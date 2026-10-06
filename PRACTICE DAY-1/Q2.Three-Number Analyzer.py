a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))
largest = max(a, b, c)
smallest = min(a, b, c)
average = (a + b + c) / 3
print("The Largest number is :", largest)
print("The Smallest number is:", smallest)
print(f"Average: {average:.2f}")
# Read a separate number as an another input
n = int(input("Enter a number for classification: "))
# using nested conditions
if n > 0:
    if n % 2 == 0:
        print("Classification: Positive and Even")
    else:
        print("Classification: Positive and Odd")
elif n < 0:
    if n % 2 == 0:
        print("Classification: Negative and Even")
    else:
        print("Classification: Negative and Odd")
else:
    print("Classification: Zero")