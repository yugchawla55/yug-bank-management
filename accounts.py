# accounts.py
# Everything to do with creating and looking up accounts.
#
# An account is just a dict like this:
#   {"account_number": 1001, "name": "Asha Verma", "balance": 500.0}
# Nothing fancy - a proper class felt like overkill for something
# this small, and dicts serialize straight to JSON anyway.

from storage import load_accounts, save_accounts


def _next_account_number(accounts):
    # first account starts at 1001 just so it looks a bit more like
    # a real account number instead of starting from 1
    if not accounts:
        return 1001
    return max(a["account_number"] for a in accounts) + 1


def create_account(name, opening_balance):
    accounts = load_accounts()
    account = {
        "account_number": _next_account_number(accounts),
        "name": name,
        "balance": round(opening_balance, 2),
    }
    accounts.append(account)
    save_accounts(accounts)
    return account


def find_account(account_number):
    for acc in load_accounts():
        if acc["account_number"] == account_number:
            return acc
    return None


def update_balance(account_number, new_balance):
    accounts = load_accounts()
    for acc in accounts:
        if acc["account_number"] == account_number:
            acc["balance"] = round(new_balance, 2)
            break
    save_accounts(accounts)


def list_all_accounts():
    return load_accounts()
