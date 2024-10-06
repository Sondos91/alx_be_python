# main-0.py

import sys
from bank_account import BankAccount

def main():
    # Initialize the account with a starting balance of $100
    account = BankAccount(100)

    # Check if enough arguments are provided
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    # Split the command from the argument
    command, *params = sys.argv[1].split(':')
    
    # Check if amount is provided and convert to float if it exists
    amount = float(params[0]) if params else None

    # Handle different commands
    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount:.2f}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount:.2f}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()
