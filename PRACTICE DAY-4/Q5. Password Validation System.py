password = input("enter you password:")
uppercase = False
lowercase = False
digit = False
special = False
for ch in password:
    if ch.isupper():
        uppercase = True
    elif ch.islower():
        lowercase = True
    elif ch.isdigit():
        digit = True
    else:
        special = True
if len(password) >= 8 and uppercase and lowercase and digit and special:
    print("Valid password")
else:
    print("Invalid password")
print("Uppercase:", "Present" if uppercase else "Missing")
print("Lowercase:", "Present" if lowercase else "Missing")
print("Digit:", "Present" if digit else "Missing")
print("Special character:", "Present" if special else "Missing")
print("Minimum length:", "Satisfied" if len(password) >= 8 else "Not satisfied")