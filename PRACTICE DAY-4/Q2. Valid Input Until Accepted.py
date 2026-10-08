invalid = 0
while True:
    num = int(input("enter the number:"))
    if num < 1 or num > 100:
        print("Invalid input")
        invalid += 1
        continue
    print("Accepted value:", num)
    print("Invalid attempts:", invalid)
    break