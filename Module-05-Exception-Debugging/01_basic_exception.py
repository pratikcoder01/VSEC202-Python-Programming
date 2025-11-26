"""
Demonstrates basic exception handling for division.
"""

try:
    a = float(input("Enter numerator: "))
    b = float(input("Enter denominator: "))
    result = a / b
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Please enter valid numbers.")
else:
    print(f"Result = {result}")
finally:
    print("Division operation completed.")
