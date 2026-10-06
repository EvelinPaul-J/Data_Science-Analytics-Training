prices = []
while True:
    value = input("Enter item price or Done: ")
    if value == "Done":
        break
    prices.append(float(value))
print("\nItem Price")
print("----------------")
for i in range(len(prices)):
    print(f"Item{i+1} {prices[i]:.2f}")
subtotal = sum(prices)
if subtotal >= 500:
    discount = subtotal * 10 / 100
elif subtotal >= 200:
    discount = subtotal * 5 / 100
else:
    discount = 0
amount = subtotal - discount
tax = amount * 18 / 100
final = amount + tax
print("----------------")
print(f"Subtotal = {subtotal:.2f}")
print(f"Discount = {discount:.2f}")
print(f"Tax      = {tax:.2f}")
print(f"Final    = {final:.2f}")