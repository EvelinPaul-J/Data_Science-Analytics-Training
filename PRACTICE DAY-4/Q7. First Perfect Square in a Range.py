l, r = map(int, input().split())
found = False
for num in range(l, r + 1):
    i = 1
    while i * i <= num:
        if i * i == num:
            print("First perfect square:", num)
            found = True
            break
        i += 1
    if found:
        break
if not found:
    print("No perfect square found")