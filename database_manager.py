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
        """Create a table from the create_table_sql statement.

        :param conn: Connection object
        :param table_name: name for table
        """
        try:
            sql_table = ("CREATE TABLE IF NOT EXISTS " + table_name + """(id integer PRIMARY KEY,
                                   title text NOT NULL,
                                   user text NOT NULL,
                                   link text NOT NULL);""")
            c = conn.cursor()
            c.execute(sql_table)
            self.table = table_name
        except Error as e:
            print(e)

    def create_row(self, conn, post):
        """Create a new row into the table.

        :param conn:
        :param post: 3 values (title,user,link)
        :return: post id
        """
        sql_insert = (' INSERT INTO ' + self.table + '''(title,user,link)
        VALUES(?,?,?)''')
        # sql = sql_insert + '(title,user,link) VALUES(?,?,?) '
        cur = conn.cursor()
        cur.execute(sql_insert, post)
        conn.commit()
        return cur.lastrowid

    def delete_row(self, conn, id):
        """Delete a task by id.

        :param conn:
        :param id: ID of task
        """
        sql_del = ("DELETE FROM " + self.table + "WHERE id=?")
        cur = conn.cursor()
        cur.execute(sql_del, (id))

    def get_random_row(self, conn, id):
        """Return a random id within the database limit.

        :param conn:
        :param id:
        """
        tot_rows = ("SELECT Count(*) FROM " + self.table)
        return random.randrange(0, tot_rows)



# sql = (sql_table + """(id integer PRIMARY KEY,
#                        title text NOT NULL,
#                        user text NOT NULL,
#                        link text NOT NULL);""")
