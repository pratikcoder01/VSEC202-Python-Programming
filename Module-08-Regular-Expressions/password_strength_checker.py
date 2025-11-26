"""
Simple password strength checker using regex.
Conditions (example):
- at least 8 characters
- at least one uppercase letter
- at least one lowercase letter
- at least one digit
- at least one special character
"""

import re


def is_strong(password):
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"\d", password):
        return False
    if not re.search(r"[@$!%*?&]", password):
        return False
    return True


pwd = input("Enter password: ")
if is_strong(pwd):
    print("Strong password.")
else:
    print("Weak password. Try adding uppercase, lowercase, digits and special characters.")
