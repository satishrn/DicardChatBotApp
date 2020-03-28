import sqlite3


class DataStoreSqlite(object):
    """ Database class to create , insert and fetch the data """
    def __init__(self):
        self.conn = sqlite3.connect('search.sqlite')   # connecting to database and creating table
        self.cur = self.conn.cursor()
        self.table = self.cur.execute('CREATE TABLE if not exists SearchModel(value text)')

    def insert_values(self, value):
        self.cur.execute('insert into SearchModel values(?)', (value,))
        self.conn.commit()

    # Fetching the distinct column value
    def fetch_value(self):
        return self.cur.execute('SELECT DISTINCT value FROM SearchModel').fetchall()

    def remove_duplicates(self):
        pass


# We can create different database also an store that object here
database_obj = DataStoreSqlite()
