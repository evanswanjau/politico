""" The user module that is supposed to take care of all user methods and attributes """
import psycopg2
from psycopg2 import Error
from app.db.database import DBConnection

class UserModule():
    """ All user processes class """

    db = DBConnection()

    def __init__(self, data=None):
        self.data = data

    # signup user
    def signupUser(self):
        """ signup user """
        validated_object = self.data
        # add to db
        db.insert_data(validated_object)
        return [{"token": "#token", "user":validated_object}]


    # login user
    def loginUser(self):
        """ login user """
        validated_data = self.data

        query = """SELECT * FROM users WHERE email = {}""".format(validated_data["email"])
        user = db.fetch_single_item(query)
        if user:
            # validate password
        else:
            raise NotFoundError('user doesn\'t exist')
        return [{"token": "#token", "user":user}]


    # express interest

    # vote

    # get political party results

    # petition
