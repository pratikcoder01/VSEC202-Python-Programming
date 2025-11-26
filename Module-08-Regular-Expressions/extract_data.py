"""
Example of data extraction using regex.
Extracts all numbers from given text.
"""

import re

text = input("Enter some text with numbers: ")
numbers = re.findall(r"\d+\.?\d*", text)

if numbers:
    print("Numbers found in text:")
    for n in numbers:
        print(n)
else:
    print("No numbers found.")
