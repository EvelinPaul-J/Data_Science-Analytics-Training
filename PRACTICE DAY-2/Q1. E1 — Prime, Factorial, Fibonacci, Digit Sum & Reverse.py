n = int(input("Enter N: "))
number = int(input("Enter Number: "))
print("Primes:", end=" ")
for num in range(2, n + 1):
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break
    if prime:
        print(num, end=" ")
factorial = 1
for i in range(1, n + 1):
    factorial = factorial * i
print("\nFactorial:", factorial)
a = 0
b = 1
print("Fibonacci:", end=" ")
for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c
temp = number
digit_sum = 0
reverse = 0
while temp > 0:
    digit = temp % 10
    digit_sum = digit_sum + digit
    reverse = reverse * 10 + digit
    temp = temp // 10
print("\nDigit Sum:", digit_sum)
print("Reverse:", reverse)