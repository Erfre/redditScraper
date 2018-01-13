"""This class handles all the connections to the database."""
import random
import sqlite3
from sqlite3 import Error


class db_manager(object):
    """docstring for db_manager.

    This class handles all the connections to the database.
    """

    def __init__(self, dir_db):
        """Initilize.

        :param dir_db: directory for database
        """
        super(db_manager, self).__init__()
        self.dir_db = dir_db
        self.table = ""

    def create_connect(self):
        """Create db connection to sqlite."""
        try:
            conn = sqlite3.connect(self.dir_db)
            return conn
        except Error as e:
            print(e)

        return None

    def get_row(self, conn, id):
        """Return row based on id"""
        cur = conn.cursor()
        cur.exectute('SELECT * FROM ' + self.table + ' WHERE id=?', (id,))
        tot_rows = cur.fetchall()
        if len(tot_rows) <= id:
            return cur.fetchone()
        else:
            print("Id is out of range " + str(len(tot_rows)))
            return