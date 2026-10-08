n = int(input("Enter N: "))

print("\nRight Triangle")
for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()
print("\nNumber Triangle")
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()

print("\nMultiplication Grid")
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}", end="   ")
    print()