"""
Prime number analyzer.
1. Check if a number is prime
2. Print all primes up to a given number
"""

def is_prime(num):
    """Return True if num is prime, else False."""
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


print("=== Prime Number Analyzer ===")
print("1. Check if a number is prime")
print("2. List all primes up to N")

choice = input("Enter your choice (1/2): ")

if choice == "1":
    n = int(input("Enter a number: "))
    if is_prime(n):
        print(f"{n} is a prime number.")
    else:
        print(f"{n} is not a prime number.")
elif choice == "2":
    n = int(input("Enter N: "))
    print(f"Prime numbers up to {n}:")
    for num in range(2, n + 1):
        if is_prime(num):
            print(num, end=" ")
    print()
else:
    print("Invalid choice.")
