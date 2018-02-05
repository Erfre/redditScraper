"""This class handles all the connections to the database."""
import random
import sqlite3
from sqlite3 import Error
from random import randint


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
        self.max_id = None

    def create_connect(self):
        """Create db connection to sqlite."""
        try:
            conn = sqlite3.connect(self.dir_db)
            return conn
        except Error as e:
            print(e)

        return None

    def count_row(self, conn):
        """Retrieves the max id in the table"""
        cur = conn.cursor()
        cur.execute('SELECT max(id) FROM ' + self.table)
        max = cur.fetchone()[0]
        self.max_id = max
        return

    def get_random_row(self, conn):
        # Might not work when a row is deleted if its based on id?
        # Solved by using a while loop atm.
        """Return random row from table"""
        cur = conn.cursor()

        while True:
            id = randint(0, self.max_id)
            try:
                cur.execute('SELECT * FROM ' + self.table + """ WHERE id=:rand
                AND reviewed=:rv""", {"rand": id, "rv": 0})
                return cur.fetchone()
            except:
                print("Looks like this id doesn't exist")
                continue

    def update_desc(self, conn, id, desc):
        """Updates the title with a description of the image."""
        cur = conn.cursor()
        cur.execute('UPDATE ' + self.table + ' SET title=:desc ,reviewed=:rv WHERE id=:id',
                    {"desc": desc, "rv": "1", "id": id})
        conn.commit()

    def delete_row(self, conn, id):
        """Deletes entry in database"""
        cur = conn.cursor()
        cur.execute('DELETE FROM '+ self.table +' WHERE id=:id', {"id":id})
        conn.commit()