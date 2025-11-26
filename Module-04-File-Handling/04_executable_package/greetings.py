"""
Simple module inside a package.
"""

def say_hello(name: str) -> None:
    print(f"Hello, {name}! This is a function from a Python package.")


if __name__ == "__main__":
    user_name = input("Enter your name: ")
    say_hello(user_name)
