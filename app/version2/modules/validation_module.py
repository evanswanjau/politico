""" This is our app's security. No weapon formed against us shall prosper!!! """
import os
from ...error_handlers import *
from app.db.database import DBConnection
DB_URL = os.getenv("DATABASE_URL")
db = DBConnection(DB_URL)

class DataValidation():
    """ This is our data validation methods and attributes """

    # validate_fields
    def validateFields(field, data):
        data = [key for key in data]
        if field not in data:
            raise ValidationError(field + ' field does not exist')

        return False

    # validate empty
    def validateEmpty(key, value):
        if not value or str(value).strip() == "":
            raise ValidationError(key + ' cannot be empty')
        else:
            return False

    # validate existence
    def validateExistence(table, key, value):
        item_query = """ SELECT * FROM {} WHERE {} = '{}'""".format(table, key, value)
        item = db.fetch_single_item(item_query)
        if item:
            return item
        else:
            return False

    # validate type
    def validateType(value, type):
        if not isinstance(value, type):
            raise ValidationError('incorrect value type, must be ' + str(type.__name__))
        else:
            return False

    # validate length
    def validate_length(key, value, min_length, max_length):
        if len(value) < min_length:
            raise ValidationError(key + ' can\'t be less than ' + str(min_length) + ' characters.')
        elif len(value) > max_length:
            raise ValidationError(key + ' can\'t be greater than ' + str(max_length) + ' characters.')
        else:
            return False
