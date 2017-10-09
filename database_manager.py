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

    def create_table(self, conn, table_name):
        """Create a table with the CREATE TABLE sql statement.

        :param conn: Connection to database
        :param table_name: name for table
        """
        try:
            sql_table = ("CREATE TABLE IF NOT EXISTS " + table_name + """
                                  (id INTEGER PRIMARY KEY,
                                   path text NOT NULL,
                                   description text NOT NULL,
                                   reviewed INTEGER NOT NULL,
                                   url text NOT NULL);""")
            c = conn.cursor()
            c.execute(sql_table)
            self.table = table_name
        except Error as e:
            print(e)

    def create_row(self, conn, post):
        """Create a new row into the table.

        :param conn:
        :param post: 3 string values (path,description, reviewed)
        :return: post id
        """
        sql_insert = (' INSERT INTO ' + self.table + '''(path, description, reviewed, url)
        VALUES(?,?,?, ?)''')
        cur = conn.cursor()
        cur.execute(sql_insert, post)
        conn.commit()
        return cur.lastrowid
