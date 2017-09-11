"""Retrives the account info from json file."""
import json


def load_json(file):
    """Load json file."""
    with open(file) as account_file:
        accounts = json.load(account_file)
    return accounts


def get_reddit():
    """Retrives data for reddit accounts."""
    accounts = {}
    account_data = load_json("accounts.json")

    for account in account_data["reddit"]:
        accounts.update(account)

    return accounts
