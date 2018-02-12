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
                                   title text NOT NULL,
                                   user text NOT NULL,
                                   url text NOT NULL,
                                   num_pics INTEGER NOT NULL,
                                   reviewed INTEGER NOT NULL);""")
            c = conn.cursor()
            c.execute(sql_table)
            self.table = table_name
        except Error as e:
            print(e)

    def create_row(self, conn, post):
        """Create a new row into the table.

        :param conn:
        :param post: 5 string values (path,description, reviewed)
        :return: post id
        """
        sql_insert = (' INSERT INTO ' + self.table + '''(path, title, user, url, num_pics, reviewed)
        VALUES(?,?,?,?,?,?)''')
        cur = conn.cursor()
        cur.execute(sql_insert, post)
        conn.commit()
        return cur.lastrowid

    def find_duplicate(self, conn):
        sql_delete = "DELETE FROM " + self.table + " WHERE ID NOT IN (SELECT MIN(id) id FROM " + self.table + \
                     " GROUP BY id, path);"
        cur = conn.cursor()
        cur.execute(sql_delete)
        return cur

    def count_row(self, conn):
        """Retrieves the max id in the table"""
        cur = conn.cursor()
        cur.execute('SELECT max(id) FROM ' + self.table)
        max = cur.fetchone()[0]
        self.max_id = max
        return max

    def get_random_row(self, conn):
        """Return random row from table"""
        cur = conn.cursor()

        while True:
            id = randint(1, self.max_id)
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
        cur.execute('DELETE FROM ' + self.table + ' WHERE id=:id', {"id": id})
        conn.commit()
