n = int(input())
numbers = list(map(int, input().split()))

n = len(numbers)

current = numbers[0]
current_count = 1
best = numbers[0]
best_count = 1

for i in range(1, n):
    if numbers[i] == current:
        current_count += 1
    else:
        current = numbers[i]
        current_count = 1

    if current_count > best_count:
        best_count = current_count
        best = current

print("Value =", best)
print("Length =", best_count)