message = input("Message: ")
shift = int(input("Shift: "))
encrypted = ""
for ch in message:
    if ch.isupper():
        encrypted += chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
    elif ch.islower():
        encrypted += chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
    else:
        encrypted += ch
decrypted = ""
for ch in encrypted:
    if ch.isupper():
        decrypted += chr((ord(ch) - ord('A') - shift) % 26 + ord('A'))
    elif ch.islower():
        decrypted += chr((ord(ch) - ord('a') - shift) % 26 + ord('a'))
    else:
        decrypted += ch
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)