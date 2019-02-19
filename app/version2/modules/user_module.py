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
        # validate data using jwt
        validated_object = self.data
        # add to db
        db.insert_data(validated_object)
        return [{"token": "#token", "user":validated_object}]


    # login user

    # express interest

    # vote

    # get political party results

    # petition
