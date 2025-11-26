"""
Simple Interest Calculator.
SI = (P * R * T) / 100
"""

principal = float(input("Enter principal amount (P): "))
rate = float(input("Enter rate of interest (R) in %: "))
time = float(input("Enter time (T) in years: "))

simple_interest = (principal * rate * time) / 100

print(f"Simple Interest = {simple_interest:.2f}")
print(f"Total Amount = {principal + simple_interest:.2f}")
