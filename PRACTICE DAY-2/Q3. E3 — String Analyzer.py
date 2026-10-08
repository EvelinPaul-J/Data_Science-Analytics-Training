text = input("Enter a string: ")
reverse = ""
for i in range(len(text) - 1, -1, -1):
    reverse = reverse + text[i]
slice_reverse = text[::-1]
print("Loop Reverse:", reverse)
print("Slice Reverse:", slice_reverse)
clean = ""
for ch in text:
    if ch != " ":
        clean = clean + ch.lower()
if clean == clean[::-1]:
    print("Palindrome: Yes")
else:
    print("Palindrome: No")
vowels = 0
consonants = 0
digits = 0
for ch in text.lower():
    if ch in "aeiou":
        vowels += 1
    elif ch.isalpha():
        consonants += 1
    elif ch.isdigit():
        digits += 1
print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)