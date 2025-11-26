"""
Calculates the factorial of a given non-negative integer.
"""

n = int(input("Enter a non-negative integer: "))

if n < 0:
    print("Factorial is not defined for negative numbers.")
else:
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print(f"Factorial of {n} is {fact}")
