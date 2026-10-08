name = input("Enter Customer Name: ")
units = int(input("Enter Units: "))
if units <= 100:
    amount = units * 2
elif units <= 200:
    amount = (100 * 2) + ((units - 100) * 3)
else:
    amount = (100 * 2) + (100 * 3) + ((units - 200) * 10)
print("\nElectricity Bill")
print("Customer :", name)
print("Units    :", units)
print(f"Amount   : ₹{amount:.2f}")