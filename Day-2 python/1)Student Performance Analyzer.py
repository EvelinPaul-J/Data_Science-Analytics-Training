def analyze_student(records):
    qualified=[]
    topper=records[0][0]
    high_total=0
    for element in records:
        name=element[0]
        total=element[1]+element[2]+element[3]
        average=total/3
        if average>=75:
            qualified.append(name)
        if total>high_total:
            total=high_total
            topper=name
    return{"Qualified":qualified,"Topper":topper}
records = [
    ("Asha", 85, 78, 92),
    ("Bala", 65, 72, 70),
    ("Charan", 90, 88, 95),
    ("Divya", 76, 80, 74),
    ("Esha", 60, 68, 72)
]
result=analyze_student(records)
print(result)