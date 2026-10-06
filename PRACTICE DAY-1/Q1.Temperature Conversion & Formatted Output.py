celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32
kelvin = celsius + 273.15
# Printing the  converted temperature
print(f"Celsius: {celsius:.2f}°C")
print(f"Fahrenheit: {fahrenheit:.2f}°F")
print(f"Kelvin: {kelvin:.2f}K")
print("\nConversion Table")
print("Celsius    Fahrenheit    Kelvin")
# Print table from -40°C to 100°C as per the rule(start,stop,step)
for c in range(-40, 101, 10):
    f = (c * 9 / 5) + 32
    k = c + 273.15
    #printing with aligment for table
    print(f"{c:7.2f}    {f:10.2f}    {k:8.2f}")