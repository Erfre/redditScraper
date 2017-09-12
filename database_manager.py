"""This class handles all the connections to the database."""
import sqlite3
from sqlite3 import Error


class db_manager(object):
    """docstring for db_manager."""

    def __init__(self, database):
        """Initilize."""
        super(db_manager, self).__init__()
        self.database = database

    def connect(self):
        """Create db connection to sqlite."""
        try:
            conn = sqlite3.connect(self.database)
            return conn
        except Error as e:
            print(e)

        return None
