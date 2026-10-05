def clean_data(data):
    result = []
    for record in data:
        parts = record.strip().split(",")
        name = parts[0].strip().title()
        city = parts[1].strip().title()
        age = int(parts[2].strip())
        customer = {
            "name": name,
            "city": city,
            "age": age
        }
        if customer not in result:
            result.append(customer)
    return result
data = [
    " Asha, Chennai, 25 ",
    "Bala, chennai, 30",
    " asha, Chennai, 25",
    "Charan, Bangalore, 28",
    "Bala, Chennai, 30 "
]
print(clean_data(data))