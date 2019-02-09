""" A class to handle government office methods """
from flask import abort
from .party_module import PoliticalParty

class GovernmentOffice():

    """ Methods and Attributes for GovernmentOffice. """

    def __init__(self, office_id=None, office_type=None, name=None, office_data=None):
        self.office_id = office_id
        self.office_type = office_type
        self.name = name
        self.office_data = office_data


    def create_office(self):
        """ This Method Will Take Care of Validating Office Data """
        # id
        if not self.office_id:
            abort(400)
        else:
            if PoliticalParty.check_existence(self, "office_id", self.office_id, self.office_data):
                abort(409)
            else:
                office_id = self.office_id

        # office_type
        if not self.office_type:
            abort(400)
        else:
            office_type = self.office_type


        # name
        if not self.name:
            abort(400)
        else:
            if PoliticalParty.check_existence(self, "name", self.name, self.office_data):
                abort(409)
            else:
                name = self.name


        return {
            "id": office_id,
            "type": office_type,
            "name": name,
        }


    def get_specific_government_office(self, office_id):
        """ This method gets specific government office """
        if not PoliticalParty.check_existence(self, "id", office_id, self.office_data):
            abort(400)
        else:
            for i in self.office_data:
                if i.get("id") == office_id:
                    office_data = i
                    break


        return [office_data]
