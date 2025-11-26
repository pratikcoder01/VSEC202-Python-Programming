"""
Identifies whether a character is:
- alphabet (vowel / consonant)
- digit
- special character
"""

ch = input("Enter a single character: ")

if len(ch) != 1:
    print("Please enter exactly one character.")
else:
    if ch.isalpha():
        print("It is an alphabet.")
        if ch.lower() in "aeiou":
            print("It is a vowel.")
        else:
            print("It is a consonant.")
    elif ch.isdigit():
        print("It is a digit.")
    else:
        print("It is a special character.")
