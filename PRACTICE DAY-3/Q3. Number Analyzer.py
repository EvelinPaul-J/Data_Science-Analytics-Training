start = int(input("Start: "))
end = int(input("End: "))
print("Number\tPrime\tPerfect\tArmstrong\tPalindrome\tDigit Sum\tDigits\tBinary")
for n in range(start, end + 1):
    if n < 2:
        prime = "No"
    else:
        prime = "Yes"
        for i in range(2, n):
            if n % i == 0:
                prime = "No"
                break
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    perfect = "Yes" if total == n else "No"
    temp = n
    digits = 0
    digit_sum = 0
    while temp > 0:
        digit = temp % 10
        digit_sum += digit
        digits += 1
        temp //= 10
    temp = n
    armstrong_sum = 0
    while temp > 0:
        digit = temp % 10
        armstrong_sum += digit ** digits
        temp //= 10
    armstrong = "Yes" if armstrong_sum == n else "No"
    reverse = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        reverse = reverse * 10 + digit
        temp //= 10
    palindrome = "Yes" if reverse == n else "No"
    binary = bin(n)[2:]
    print(n, "\t", prime, "\t", perfect, "\t", armstrong, "\t\t", palindrome, "\t\t", digit_sum, "\t\t", digits, "\t", binary)