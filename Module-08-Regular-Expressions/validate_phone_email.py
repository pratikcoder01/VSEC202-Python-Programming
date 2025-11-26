"""
Validates phone number and email using regular expressions.
"""

import re

phone_pattern = re.compile(r"^[6-9]\d{9}$")  # simple Indian mobile pattern
email_pattern = re.compile(r"^[\w\.-]+@[\w\.-]+\.\w+$")

phone = input("Enter phone number: ")
email = input("Enter email address: ")

if phone_pattern.match(phone):
    print("Valid phone number.")
else:
    print("Invalid phone number.")

if email_pattern.match(email):
    print("Valid email address.")
else:
    print("Invalid email address.")
