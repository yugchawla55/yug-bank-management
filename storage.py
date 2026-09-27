# storage.py
# Small helper module that deals with reading/writing the JSON files
# on disk. Everything else in the project goes through here instead
# of opening files directly - keeps the file paths in one place.

import json
import os

DATA_DIR = "data"
ACCOUNTS_FILE = os.path.join(DATA_DIR, "accounts.json")
TRANSACTIONS_FILE = os.path.join(DATA_DIR, "transactions.json")


def _make_data_dir():
    # runs on every load/save call, but os.makedirs with exist_ok
    # is cheap enough that it doesn't matter
    os.makedirs(DATA_DIR, exist_ok=True)


def _read_json(path):
    _make_data_dir()
    if not os.path.exists(path):
        return []
    with open(path, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            # empty or corrupted file - just treat it as no data
            # rather than crashing the whole program
            return []


def _write_json(path, data):
    _make_data_dir()
    with open(path, "w") as f:
        json.dump(data, f, indent=4)


def load_accounts():
    return _read_json(ACCOUNTS_FILE)


def save_accounts(accounts):
    _write_json(ACCOUNTS_FILE, accounts)


def load_transactions():
    return _read_json(TRANSACTIONS_FILE)


def save_transactions(transactions):
    _write_json(TRANSACTIONS_FILE, transactions)
