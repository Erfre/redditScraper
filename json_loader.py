import json

def load_json(file):
    """Load json file"""
    with open(file) as load_file:
        loaded_file = json.load(load_file)
    return loaded_file

def get_settings():
    """Retrieves settings from json file."""
    settings = load_json("setting.json")

    db_path = settings["db_path_name"]
    db_table = settings["db_table_name"]

    return db_path, db_table
