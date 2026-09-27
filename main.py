# main.py
# Entry point - just a text menu that wires user input to the
# functions in the other files. Run with: python main.py

from accounts import create_account, find_account, list_all_accounts
from statements import generate_statement
from transactions import deposit, transfer, withdraw


def print_menu():
    print("\n----- YUG'S BANK -----")
    print("1. Create Account")
    print("2. View Account")
    print("3. List All Accounts")
    print("4. Deposit")
    print("5. Withdraw")
    print("6. Transfer")
    print("7. Month-End Statement")
    print("8. Exit")


def get_amount(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def get_account_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid account number (whole number).")


def handle_create_account():
    name = input("Enter account holder name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    opening_balance = get_amount("Enter opening deposit amount: ")
    account = create_account(name, opening_balance)
    print(f"Account created! Account Number: {account['account_number']}")


def handle_view_account():
    acc_no = get_account_number("Enter account number: ")
    account = find_account(acc_no)
    if account is None:
        print("Account not found.")
        return
    print(f"Account Number: {account['account_number']}")
    print(f"Name          : {account['name']}")
    print(f"Balance       : {account['balance']:.2f}")


def handle_list_accounts():
    accounts = list_all_accounts()
    if not accounts:
        print("No accounts yet.")
        return
    print(f"\n{'Acc No':<10}{'Name':<20}{'Balance':>10}")
    for acc in accounts:
        print(f"{acc['account_number']:<10}{acc['name']:<20}{acc['balance']:>10.2f}")


def handle_deposit():
    acc_no = get_account_number("Enter account number: ")
    amount = get_amount("Enter deposit amount: ")
    _, message = deposit(acc_no, amount)
    print(message)


def handle_withdraw():
    acc_no = get_account_number("Enter account number: ")
    amount = get_amount("Enter withdrawal amount: ")
    _, message = withdraw(acc_no, amount)
    print(message)


def handle_transfer():
    from_acc = get_account_number("Enter your account number: ")
    to_acc = get_account_number("Enter recipient account number: ")
    amount = get_amount("Enter transfer amount: ")
    _, message = transfer(from_acc, to_acc, amount)
    print(message)


def handle_statement():
    acc_no = get_account_number("Enter account number: ")
    month = int(input("Enter month (1-12): "))
    year = int(input("Enter year (e.g. 2026): "))
    generate_statement(acc_no, month, year)


MENU_ACTIONS = {
    "1": handle_create_account,
    "2": handle_view_account,
    "3": handle_list_accounts,
    "4": handle_deposit,
    "5": handle_withdraw,
    "6": handle_transfer,
    "7": handle_statement,
}


def main():
    while True:
        print_menu()
        choice = input("Choose an option (1-8): ").strip()

        if choice == "8":
            print("Thank you for using Yug's Bank. Goodbye!")
            break

        action = MENU_ACTIONS.get(choice)
        if action is None:
            print("Invalid choice. Please pick a number from 1 to 8.")
        else:
            action()


if __name__ == "__main__":
    main()
