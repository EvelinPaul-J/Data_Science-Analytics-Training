age = int(input("Enter the customer's age: "))
voting = "This age is Eligible to Vote" if age >= 18 else " This age is Not Eligible to Vote"
#if the customer age is greater than 60 provide senior citizen discount
discount = "20% Senior Citizen Discount" if age >= 60 else "No Senior Citizen Discount"
print(voting)
print(discount)