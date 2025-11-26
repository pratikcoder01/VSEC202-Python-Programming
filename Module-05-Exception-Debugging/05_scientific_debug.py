"""
Simple scientific calculation with error handling.
Calculates velocity v = d / t
"""

try:
    distance = float(input("Enter distance (meters): "))
    time = float(input("Enter time (seconds): "))
    if time == 0:
        raise ZeroDivisionError("Time cannot be zero.")
    velocity = distance / time
except ValueError:
    print("Please enter valid numbers.")
except ZeroDivisionError as e:
    print("Error:", e)
else:
    print(f"Velocity = {velocity} m/s")
