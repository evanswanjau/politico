""" A class to handle the political party object """
import psycopg2, re, os
from app.db.database import DBConnection
from app.version2.modules.validation_module import DataValidation as dv
from ...error_handlers import *
DB_URL = os.getenv("DATABASE_URL")
db = DBConnection(DB_URL)


class PoliticalParty():

    """ Methods and Attrinutes for PoliticalParty. """

    def __init__(self, data=None):
        self.data = data


    def create_party(self):
        """ validate the political party data """

        expected_fields = ['name', 'hqAddress', 'logoUrl']

        for field in expected_fields:
            dv.validateFields(field, self.data)

        # validate not empty and type
        for key in self.data:
            dv.validateEmpty(key, self.data[key])
            dv.validateType(key, self.data[key], str)
            if dv.validateExistence('party', key, self.data[key]):
                raise NotAcceptable(key + ' ' + self.data[key] + ' already exists')

        db.insert_data('party', self.data)

        return self.data


    def get_all_political_parties(self):
        """ This method gets all political parties """
        party_list = []
        query = """ SELECT * FROM party  """
        parties = db.fetch_multiple_items(query)

        for party in parties:
            party_list.append({"id":party[0], "name":party[1], "logoUrl":party[2]})

        return party_list


    def get_specific_political_party(self, party_id):
        """ This method gets specific political party """

        dv.validateType('id', party_id, int)
        dv.validateEmpty('id', party_id)
        if not dv.validateExistence('party', 'id', party_id):
            raise NotFoundError('That politiclal party does not exist')
        else:
            query = """ SELECT * FROM party WHERE id = {} """.format(party_id)
            party = db.fetch_single_item(query)

        return [{"id":party[0], "name":party[1], "logoUrl":party[3]}]


    def edit_political_party(self, party_id):
        """ This method edits a specific political party """
        # validate value
        dv.validateType('party id', party_id, int)

        if not dv.validateExistence('party', 'id', party_id):
            raise NotFoundError('That politiclal party does not exist')
        else:
            #to be input
            dv.validateFields('name', self.data)
            dv.validateType('name', self.data['name'], str)
            dv.validateEmpty('name', self.data['name'])

            if dv.validateExistence('party', 'name', self.data['name']):
                raise ConflictError('party name ' + self.data['name'] + ' has been taken')
            else:
                db.update_data('party', 'name', self.data['name'], 'id', party_id)

        return [{"id":party_id, "name":self.data['name']}]


    def delete_political_party(self, party_id):
        """ This method deletes a specific political party """
        # validate value
        dv.validateType('party id', party_id, int)

        if not dv.validateExistence('party', 'id', party_id):
            raise NotFoundError('That politiclal party does not exist')
        else:
            db.delete_data('party', 'id', party_id)

        return ["deletion successful"]
