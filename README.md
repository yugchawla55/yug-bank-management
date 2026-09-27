# Bank Management System

A simple, menu-driven Bank Management System built in Python for the
CSE1021 (Introduction to Problem Solving and Programming) course project.

## Overview

This program lets a user create bank accounts, deposit and withdraw
money, transfer money between accounts, and generate a month-end
statement showing every transaction for a given month. All data is
saved to JSON files, so nothing is lost when the program is closed.

## Features

- **Account Management** — create new accounts, view a single account,
  list all accounts
- **Transaction Processing** — deposit, withdraw, and transfer between
  accounts, with validation (no negative amounts, no overdrawing)
- **Month-End Statement Generator** — pick an account, a month and a
  year, and get a formatted statement with opening balance, every
  transaction, and closing balance
- **Persistent storage** — accounts and transactions are saved to
  `data/accounts.json` and `data/transactions.json`
- **Input validation & error handling** — invalid input (letters where
  a number is expected, insufficient balance, unknown account number,
  etc.) is caught and reported instead of crashing the program

## Technologies / Tools Used

- Python 3 (standard library only — `json`, `os`, `datetime`)
- No external packages required

## Project Structure

```
bank_management_system/
├── main.py            # Entry point: text menu
├── accounts.py        # Module 1: Account Management
├── transactions.py    # Module 2: Transaction Processing
├── statements.py       # Module 3: Month-End Statement Generator
├── storage.py          # Saves/loads data to/from JSON files
├── test_bank.py        # Simple tests for the core logic
├── README.md
└── statement.md         # Problem statement, scope, target users
```

## How to Install & Run

1. Make sure Python 3 is installed (`python3 --version`).
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run:
   ```
   python3 main.py
   ```
5. Follow the on-screen menu (type a number 1-8 and press Enter).

The first time you run it, there will be no accounts — start by
choosing option 1 to create one.

## Instructions for Testing

A simple test script is included that checks account creation,
deposits, withdrawals (including rejecting an over-withdrawal) and
transfers.

Run it with:
```
python3 test_bank.py
```

You should see `PASSED` printed for each test and a final
`All tests passed!` message. Note: this creates real sample accounts
in `data/accounts.json` — delete the `data` folder afterwards if you
want to start with a clean slate before a demo.

## Example Usage

```
----- BANK MANAGEMENT SYSTEM -----
1. Create Account
2. View Account
3. List All Accounts
4. Deposit
5. Withdraw
6. Transfer
7. Month-End Statement
8. Exit
Choose an option (1-8): 1
Enter account holder name: Rahul Sharma
Enter opening deposit amount: 1000
Account created! Account Number: 1001
```

## Future Enhancements

- PIN/password protection for each account
- Interest calculation on savings accounts
- Exporting statements to a PDF or text file
