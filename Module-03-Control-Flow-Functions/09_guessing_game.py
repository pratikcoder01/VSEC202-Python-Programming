"""
Number guessing game.
The computer selects a random number between 1 and 100.
The user tries to guess it.
"""

import random

secret = random.randint(1, 100)
attempts = 0

print("I have selected a number between 1 and 100.")

while True:
    guess = int(input("Enter your guess (or 0 to quit): "))
    if guess == 0:
        print("You quit the game.")
        break

    attempts += 1

    if guess < secret:
        print("Too low! Try again.")
    elif guess > secret:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed it in {attempts} attempts.")
        break
