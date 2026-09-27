# Problem Statement

## Problem Statement

Manually tracking bank account balances and transactions is
error-prone and time-consuming, and it is hard to answer a simple
question like "what happened in my account last month?" without a
proper record. This project builds a simple console-based Bank
Management System that stores every account and every transaction,
and can generate an accurate month-end statement on demand.

## Scope of the Project

- Managing customer bank accounts (create, view, list)
- Processing deposits, withdrawals, and transfers between accounts
- Generating a month-end statement for any account, for any month
- Persisting all data to disk so it survives between program runs
- A text-based (console) interface — no GUI or web interface

Out of scope: multi-currency support, interest calculation, login
authentication, and connecting to real banks.

## Target Users

- A single bank's back-office staff who need a lightweight tool to
  manage customer accounts and transactions
- Students/reviewers evaluating this as a course project demonstrating
  functions, control flow, lists/dictionaries, and file-based data
  persistence in Python

## High-Level Features

1. **Account Management** — create an account with an opening balance,
   view one account's details, list all accounts
2. **Transaction Processing** — deposit, withdraw, and transfer money
   between accounts, with validation against invalid amounts and
   insufficient balance
3. **Month-End Statement Generator** — given an account number, month
   and year, print the opening balance, every transaction in that
   month, and the closing balance
