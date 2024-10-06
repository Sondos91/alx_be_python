# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the account with an optional initial balance (default is 0)."""
        self._account_balance = initial_balance

    def deposit(self, amount):
        """Deposit the specified amount to the account."""
        if amount > 0:
            self._account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw the specified amount if sufficient funds are available."""
        if amount > 0:
            if self._account_balance >= amount:
                self._account_balance -= amount
                return True
            else:
                return False
        else:
            print("Withdrawal amount must be positive.")
            return False

    def display_balance(self):
        """Display the current account balance in a user-friendly format."""
        print(f"Current Balance: ${self._account_balance:.2f}")
