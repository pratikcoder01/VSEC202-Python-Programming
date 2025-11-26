"""
Area calculator for basic shapes.
The user selects a shape and enters dimensions.
"""

import math

print("=== Area Calculator ===")
print("1. Circle")
print("2. Rectangle")
print("3. Triangle")

choice = input("Enter your choice (1/2/3): ")

if choice == "1":
    radius = float(input("Enter radius of the circle: "))
    area = math.pi * radius * radius
    print(f"Area of circle = {area:.2f}")
elif choice == "2":
    length = float(input("Enter length of rectangle: "))
    width = float(input("Enter width of rectangle: "))
    area = length * width
    print(f"Area of rectangle = {area:.2f}")
elif choice == "3":
    base = float(input("Enter base of triangle: "))
    height = float(input("Enter height of triangle: "))
    area = 0.5 * base * height
    print(f"Area of triangle = {area:.2f}")
else:
    print("Invalid choice.")
