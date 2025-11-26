"""
Prints Fibonacci series up to n terms.
"""

n = int(input("Enter number of terms: "))

a, b = 0, 1
count = 0

if n <= 0:
    print("Please enter a positive integer.")
else:
    print("Fibonacci sequence:")
    while count < n:
        print(a, end=" ")
        a, b = b, a + b
        count += 1
    print()
