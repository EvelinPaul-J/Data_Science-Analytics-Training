amount = int(input("Enter Withdrawal Amount: "))
if amount > 20000:
    print("Transaction rejected: Amount exceeds ₹20,000")
elif amount % 10 != 0:
    print("Transaction rejected: Amount must be a multiple of ₹10")
else:
    remaining = amount
    notes_500 = remaining // 500
    remaining = remaining % 500
    notes_200 = remaining // 200
    remaining = remaining % 200
    notes_100 = remaining // 100
    remaining = remaining % 100
    notes_50 = remaining // 50
    remaining = remaining % 50
    notes_10 = remaining // 10
    total_notes = notes_500 + notes_200 + notes_100 + notes_50 + notes_10
    print("\n₹500 notes :", notes_500)
    print("₹200 notes :", notes_200)
    print("₹100 notes :", notes_100)
    print("₹50 notes  :", notes_50)
    print("₹10 notes  :", notes_10)
    print("Total Notes:", total_notes)
    print("Amount     : ₹", amount)