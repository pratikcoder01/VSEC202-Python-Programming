"""
Identifies if a number is positive, negative or zero,
and also whether it is even or odd (for non-zero integers).
"""

num = float(input("Enter a number: "))

if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# Check even/odd only if it is an integer
if num.is_integer() and num != 0:
    if int(num) % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")
