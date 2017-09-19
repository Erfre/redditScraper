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


def get_settings():
    """Retrives settings json file."""
    settings = load_json("accounts.json")

    subreddit = settings["subreddit"]
    db_path = settings["db_path_name"]
    time_filter = settings["time_filter"]
    img_path = settings["img_path"]

    return subreddit, db_path, time_filter, img_path
