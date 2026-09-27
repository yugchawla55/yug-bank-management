# statements.py
# Builds the month-end statement: opening balance, list of
# transactions for that month, then closing balance.

from accounts import find_account
from transactions import get_transactions_for_account


def _signed_amount(txn):
    # deposits/incoming transfers add to the balance, everything
    # else subtracts from it - used to work backwards to the
    # opening balance below
    if txn["type"] in ("DEPOSIT", "TRANSFER_IN"):
        return txn["amount"]
    return -txn["amount"]


def generate_statement(account_number, month, year):
    account = find_account(account_number)
    if account is None:
        print("Account not found.")
        return

    txns_this_month = []
    for t in get_transactions_for_account(account_number):
        txn_year, txn_month, _ = t["date"].split("-")
        if int(txn_year) == year and int(txn_month) == month:
            txns_this_month.append(t)

    print("\n" + "=" * 45)
    print(f"MONTH-END STATEMENT - {month:02d}/{year}")
    print("=" * 45)
    print(f"Account Number : {account['account_number']}")
    print(f"Account Holder : {account['name']}")
    print("-" * 45)

    if not txns_this_month:
        print("No transactions this month.")
    else:
        # the opening balance isn't stored anywhere, so back it out
        # from the first transaction's balance_after
        opening_balance = txns_this_month[0]["balance_after"] - _signed_amount(txns_this_month[0])
        print(f"Opening Balance: {opening_balance:.2f}\n")
        print(f"{'Date':<12}{'Type':<15}{'Amount':>10}{'Balance':>10}")
        for t in txns_this_month:
            print(f"{t['date']:<12}{t['type']:<15}{t['amount']:>10.2f}{t['balance_after']:>10.2f}")
        print(f"\nClosing Balance: {txns_this_month[-1]['balance_after']:.2f}")

    print(f"Current Balance: {account['balance']:.2f}")
    print("=" * 45 + "\n")
