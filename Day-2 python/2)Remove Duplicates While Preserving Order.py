numbers = [10, 20, 10, 30, 20, 40, 30, 50]
sort=[]
for i in numbers:
    if i not in sort:
        sort.append(i)
print(sort)