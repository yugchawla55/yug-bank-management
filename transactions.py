# transactions.py
# Deposits, withdrawals and transfers all live here, plus a small
# helper that logs every transaction so statements.py has something
# to read from later.
#
# A logged transaction looks like:
#   {"account_number": 1001, "type": "DEPOSIT", "amount": 200.0,
#    "balance_after": 700.0, "date": "2026-09-27"}

from datetime import date

from accounts import find_account, update_balance
from storage import load_transactions, save_transactions


def _log_transaction(account_number, txn_type, amount, balance_after):
    transactions = load_transactions()
    transactions.append({
        "account_number": account_number,
        "type": txn_type,
        "amount": round(amount, 2),
        "balance_after": round(balance_after, 2),
        "date": str(date.today()),
    })
    save_transactions(transactions)


def deposit(account_number, amount):
    if amount <= 0:
        return False, "Deposit amount must be positive."

    account = find_account(account_number)
    if account is None:
        return False, "Account not found."

    new_balance = account["balance"] + amount
    update_balance(account_number, new_balance)
    _log_transaction(account_number, "DEPOSIT", amount, new_balance)
    return True, f"Deposited {amount:.2f}. New balance: {new_balance:.2f}"


def withdraw(account_number, amount):
    if amount <= 0:
        return False, "Withdrawal amount must be positive."

    account = find_account(account_number)
    if account is None:
        return False, "Account not found."

    if amount > account["balance"]:
        return False, "Insufficient balance."

    new_balance = account["balance"] - amount
    update_balance(account_number, new_balance)
    _log_transaction(account_number, "WITHDRAW", amount, new_balance)
    return True, f"Withdrew {amount:.2f}. New balance: {new_balance:.2f}"


def transfer(from_account_number, to_account_number, amount):
    if amount <= 0:
        return False, "Transfer amount must be positive."

    if from_account_number == to_account_number:
        return False, "Cannot transfer to the same account."

    from_account = find_account(from_account_number)
    to_account = find_account(to_account_number)
    if from_account is None or to_account is None:
        return False, "One or both accounts were not found."

    if amount > from_account["balance"]:
        return False, "Insufficient balance."

    new_from_balance = from_account["balance"] - amount
    new_to_balance = to_account["balance"] + amount

    update_balance(from_account_number, new_from_balance)
    update_balance(to_account_number, new_to_balance)

    # logged as two separate entries so each account's statement
    # only shows the side of the transfer that actually affects it
    _log_transaction(from_account_number, "TRANSFER_OUT", amount, new_from_balance)
    _log_transaction(to_account_number, "TRANSFER_IN", amount, new_to_balance)

    return True, f"Transferred {amount:.2f} to account {to_account_number}."


def get_transactions_for_account(account_number):
    return [t for t in load_transactions() if t["account_number"] == account_number]
