"""
Banking example with custom exception.
"""


class InsufficientBalanceError(Exception):
    """Custom exception raised when balance is insufficient."""
    pass


class BankAccount:
    def __init__(self, holder_name, balance=0.0):
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        print(f"Deposited {amount}. New balance = {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientBalanceError("Not enough balance for this withdrawal.")
        self.balance -= amount
        print(f"Withdrew {amount}. New balance = {self.balance}")


name = input("Enter account holder name: ")
account = BankAccount(name, balance=1000)

try:
    amt = float(input("Enter amount to withdraw: "))
    account.withdraw(amt)
except InsufficientBalanceError as e:
    print("Withdrawal failed:", e)
except ValueError:
    print("Please enter a valid amount.")
