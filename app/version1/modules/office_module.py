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
        office_id = PoliticalParty.check_empty_and_check_existence(self, "id",
                                                                   self.office_id, self.office_data)
        # office type
        office_type = self.office_type if self.office_type else abort(400, 'Invalid Request')
        # office
        name = PoliticalParty.check_empty_and_check_existence(self, "name", self.name,
                                                              self.office_data)

        return {
            "id": office_id,
            "type": office_type,
            "name": name,
        }


    def get_specific_gov_office(self, office_id):
        """ This method gets specific government office """
        value = None

        for i in self.office_data:
            if i.get("id") == office_id:
                office_data = [i]
                value = True
                break
            else:
                value = False

        if not value:
            abort(400, 'Invalid Request')
        else:
            return office_data
