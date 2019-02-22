""" A class to handle government office methods """
import psycopg2, re, os
from app.db.database import DBConnection
from app.version2.modules.validation_module import DataValidation as dv
from ...error_handlers import *
DB_URL = os.getenv("DATABASE_URL")
db = DBConnection(DB_URL)

class GovernmentOffice():

    """ Methods and Attributes for GovernmentOffice. """

    def __init__(self, data=None):
        self.data = data


    def create_office(self):
        """ This Method Will Take Care of Validating Office Data """

        expected_fields = ['type', 'name']

        for field in expected_fields:
            dv.validateFields(field, self.data)

        # validate not empty and type
        for key in self.data:
            dv.validateEmpty(key, self.data[key])
            dv.validateType(key, self.data[key], str)

        if dv.validateExistence('office', 'name', self.data['name']):
            raise ConflictError('office ' + self.data['name'] + ' already exists')
        else:
            db.insert_data('office', self.data)

        return [self.data]


    def get_specific_gov_office(self, office_id):
        """ This method gets specific government office """

        dv.validateType('id', office_id, int)
        dv.validateEmpty('id', office_id)
        if not dv.validateExistence('office', 'id', office_id):
            raise NotFoundError('That government office does not exist')
        else:
            query = """ SELECT * FROM office WHERE id = {} """.format(office_id)
            office = db.fetch_single_item(query)

        return [{"id":office[0], "type":office[1], "name":office[2]}]


    def get_all_government_offices(self):
        office_list = []
        query = """ SELECT * FROM office  """
        offices = db.fetch_multiple_items(query)

        for office in offices:
            office_list.append({"id":office[0], "type":office[1], "name":office[2]})

        return office_list
