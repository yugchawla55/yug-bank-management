# test_bank.py
# Quick sanity checks for the core logic - not using pytest or
# anything, just plain asserts so it can be run directly.
#
#   python test_bank.py
#
# Heads up: this actually writes test accounts into
# data/accounts.json. Delete the data/ folder if you want a clean
# slate before demoing the project.

from accounts import create_account, find_account
from transactions import deposit, transfer, withdraw


def test_create_account():
    account = create_account("Test User A", 1000)
    assert account["balance"] == 1000
    print("test_create_account PASSED")
    return account["account_number"]


def test_deposit(acc_no):
    success, _ = deposit(acc_no, 500)
    assert success is True
    assert find_account(acc_no)["balance"] == 1500
    print("test_deposit PASSED")


def test_withdraw(acc_no):
    success, _ = withdraw(acc_no, 5000)  # too much, should fail
    assert success is False

    success, _ = withdraw(acc_no, 500)  # fine, should go through
    assert success is True
    assert find_account(acc_no)["balance"] == 1000
    print("test_withdraw PASSED")


def test_transfer(acc_no):
    account_b = create_account("Test User B", 0)
    success, _ = transfer(acc_no, account_b["account_number"], 400)
    assert success is True
    assert find_account(acc_no)["balance"] == 600
    assert find_account(account_b["account_number"])["balance"] == 400
    print("test_transfer PASSED")


if __name__ == "__main__":
    acc_no = test_create_account()
    test_deposit(acc_no)
    test_withdraw(acc_no)
    test_transfer(acc_no)
    print("\nAll tests passed!")
