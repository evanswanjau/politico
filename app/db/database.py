"""" Connection to the postgres database """
import psycopg2
from .main_db import drop_existing_tables, create_tables

class DBConnection():
    """ Connection for our entire application """

    # initialize connection
    def __init__(self, DB_URL):
        """ initilize db connection with db url """
        try:
            self.connection = psycopg2.connect(DB_URL)
            self.cursor  = self.connection.cursor()
        except Exception as error:
           print(error)


    # create tables and admin
    def create_tables_and_admin(self):
        """ creates all tables """
        tables = create_tables()

        for table in tables:
            self.cursor.execute(table)
            self.connection.commit()

        # create admin
        admin = {"firstname":"admin", "secondname":"admin", "othername":"admin",
                 "email":"admin@gmail.com", "password":"pbkdf2:sha256:50000$EVkFyv0t$352a72a9b0c37b197044db033234a96fb138264f448b8ef0de010cfd568ec3e2",
                 "phoneNumber":"0700000000", "passportUrl":"admin.img", "isAdmin":True}

        self.insert_data('users', admin)


    # drop all tables
    def drop_tables(self):
        """ Deletes all tables """
        tables = drop_existing_tables()

        for table in tables:
            self.cursor.execute(table)
            self.connection.commit()


    # fetch a single item
    def fetch_single_item(self, query):
        """ fetches a single item """
        self.cursor.execute(query)
        item = self.cursor.fetchone()
        return item


    # fetch multiple items
    def fetch_multiple_items(self, query):
        """ fetches multiple items """
        self.cursor.execute(query)
        items = self.cursor.fetchall()
        return items


    # insert data
    def insert_data(self, table, data):
        """ insert data """
        keys = ', '.join([key for key in data])
        data_values = str(tuple([data[key] for key in data]))

        self.cursor.execute(""" INSERT INTO {} ({}) VALUES
                           {} RETURNING id""".format(table, keys, data_values))
        value = self.connection.commit()
        return value

    # update data
    def update_data(self, table, key, value, field, id):
        """ update data """
        query = """ UPDATE table SET key = value WHERE field = id """
        self.cursor.execute(query)
        self.connection.commit()
