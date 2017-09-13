"""This class handles all the connections to the database."""
import sqlite3
from sqlite3 import Error


class db_manager(object):
    """docstring for db_manager."""

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
        """Create a table from the create_table_sql statement.

        :param conn: Connection object
        :param table_name: name for table
        """
        try:
            sql_table = ("CREATE TABLE IF NOT EXISTS " + table_name)
            sql = (sql_table + """(id integer PRIMARY KEY,
                                   title text NOT NULL,
                                   user text NOT NULL,
                                   link text NOT NULL);""")
            c = conn.cursor()
            c.execute(sql)
            self.table = table_name
        except Error as e:
            print(e)

    def create_row(self, conn, post):
        """Create a new row into the table.

        :param conn:
        :param post: 3 values (title,user,link)
        :return: post id
        """
        sql_insert = (' INSERT INTO ' + self.table)
        sql = sql_insert + '(title,user,link) VALUES(?,?,?) '
        cur = conn.cursor()
        cur.execute(sql, post)
        conn.commit()
        return cur.lastrowid

# Testing
# test = db_manager('/home//Databases/test/test.db')
# conn = test.create_connect()
# test.create_table(conn, "test")
# k = ("hej", "dd", "aa")
# l = ("kk", "ff", "aa")
# a = test.create_post(conn, k)
# b = test.create_post(conn, l)
