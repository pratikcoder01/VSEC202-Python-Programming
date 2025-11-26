"""
Demonstrates basic logging in Python.
Logs messages to a file named app.log
"""

import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logging.info("Application started.")

try:
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    result = x / y
except ZeroDivisionError:
    logging.error("Tried to divide by zero.")
    print("Cannot divide by zero.")
except ValueError:
    logging.error("User entered invalid integer.")
    print("Please enter valid integers.")
else:
    logging.info("Division successful.")
    print("Result:", result)
finally:
    logging.info("Application finished.")
