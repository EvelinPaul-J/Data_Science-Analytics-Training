s = input()
i = 0
while i < len(s) and s[i] == " ":
    i += 1
sign = 1
if i < len(s) and s[i] == "-":
    sign = -1
    i += 1
elif i < len(s) and s[i] == "+":
    i += 1
number = 0
found = False
while i < len(s) and s[i] >= "0" and s[i] <= "9":
    number = number * 10 + (ord(s[i]) - ord("0"))
    found = True
    i += 1
if found:
    print(sign * number)
else:
    print(0)