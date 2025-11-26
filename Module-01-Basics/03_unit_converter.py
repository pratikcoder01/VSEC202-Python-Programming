"""
Simple unit converter.
1. Centimeters to meters
2. Celsius to Fahrenheit
3. Kilograms to grams
"""

print("=== Unit Converter ===")
print("1. Centimeters to meters")
print("2. Celsius to Fahrenheit")
print("3. Kilograms to grams")

choice = input("Enter your choice (1/2/3): ")

if choice == "1":
    cm = float(input("Enter length in centimeters: "))
    meters = cm / 100
    print(f"{cm} cm = {meters} m")
elif choice == "2":
    c = float(input("Enter temperature in Celsius: "))
    f = (c * 9/5) + 32
    print(f"{c} °C = {f} °F")
elif choice == "3":
    kg = float(input("Enter weight in kilograms: "))
    grams = kg * 1000
    print(f"{kg} kg = {grams} g")
else:
    print("Invalid choice.")
