"""
Extracts all URLs from a given text using regex.
"""

import re

text = input("Enter text containing URLs: ")

url_pattern = re.compile(r"https?://[\w./-]+")
urls = url_pattern.findall(text)

if urls:
    print("Found URLs:")
    for u in urls:
        print(u)
else:
    print("No URLs found.")
