"""This class handles all the connections to the database."""
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
        self.conn = None
        self.table = ""
        self.max_id = ""
        self.min_id = ""

    def create_connect(self):
        """Create db connection to sqlite."""
        try:
            conn = sqlite3.connect(self.dir_db)
            self.conn = conn
            return
        except Error as e:
            print(e)

        return None

    def close_conn(self):
        self.conn.commit()
        self.conn.close()
        self.conn = None
        return

    def create_table(self, table_name):
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
            c = self.conn.cursor()
            c.execute(sql_table)
            self.table = table_name
        except Error as e:
            print(e)

    def create_row(self, post):
        """Create a new row into the table.

        :param conn:
        :param post: 5 string values (path,description, reviewed)
        :return: post id
        """
        sql_insert = (' INSERT INTO ' + self.table + '''(path, title, user, url, num_pics, reviewed)
        VALUES(?,?,?,?,?,?)''')
        c = self.conn.cursor()
        c.execute(sql_insert, post)
        self.conn.commit()
        return c.lastrowid

    def find_duplicate(self, user):
        sql_delete = "SELECT * FROM " + self.table + " WHERE user:=usr"
        print(type(sql_delete))

        c = self.conn.cursor()
        c.execute( "SELECT * FROM " + self.table + " WHERE user=:usr", {"usr": user})
        s = c.fetchone()
        return s

    def count_row(self):
        self.max_id = self.get_max()
        self.min_id = self.get_min()
        return

    def is_empty(self):
        sql_count = "SELECT count(*) FROM " + self.table
        c = self.conn.cursor()
        c.execute(sql_count)
        rows = c.fetchone()[0]
        return rows

    def get_max(self):
        """Retrieves the max id in the table"""
        c = self.conn.cursor()
        c.execute('SELECT max(id) FROM ' + self.table)
        max = c.fetchone()[0]
        return max

    def get_min(self):
        """Retrieves the min id in the table."""
        c = self.conn.cursor()
        c.execute('SELECT min(id) FROM ' + self.table)
        min = c.fetchone()[0]
        return min

    def get_random_row(self, reviewed):
        """Return random row from table"""
        c = self.conn.cursor()

        while True: # this needs to be the min id
            id = randint(self.min_id, self.max_id)
            print(id)
            try:
                c.execute('SELECT * FROM ' + self.table + """ WHERE id=:rand
                  AND reviewed=:rv""", {"rand": id, "rv": reviewed})
                return c.fetchone()
            except (KeyboardInterrupt, SystemExit):
                raise
            except:
                print("Looks like this id doesn't exist")
                continue

    def update_desc(self, id, desc):
        """Updates the title with a description of the image."""
        c = self.conn.cursor()
        c.execute('UPDATE ' + self.table + ' SET title=:desc ,reviewed=:rv WHERE id=:id',
                    {"desc": desc, "rv": "1", "id": id})
        self.conn.commit()
        return

    def delete_row(self, id):
        """Deletes entry in database"""
        c = self.conn.cursor()
        c.execute('DELETE FROM ' + self.table + ' WHERE id=:id', {"id": id})
        self.conn.commit()
