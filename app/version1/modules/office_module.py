""" A class to handle government office methods """
from flask import abort
from .party_module import PoliticalParty

class GovernmentOffice(PoliticalParty):

    """ Methods and Attributes for GovernmentOffice. """

    def __init__(self, id=None, type=None, name=None, office_data=None):
        self.id = id
        self.type = type
        self.name = name
        self.office_data = office_data


    def create_office(self):

        # id
        if not self.id:
            abort(400)
        else:
            if GovernmentOffice.check_existence(self, "id", self.id, self.office_data):
                abort(409)
            else:
                id = self.id

        # type
        if not self.type:
            abort(400)
        else:
            type = self.type


        # name
        if not self.name:
            abort(400)
        else:
            if GovernmentOffice.check_existence(self, "name", self.name, self.office_data):
                abort(409)
            else:
                name = self.name


        return {
            "id": id,
            "type": type,
            "name": name,
        }


    def get_all_government_offices(self):
        """ This method gets all government offices """
        offices = []
        office_data = self.office_data
        for i in office_data:
            new_dict = {"id":i["id"], "type":i["type"], "name":i["name"]}
            offices.append(new_dict)

        return offices


    def get_specific_government_office(self, id):
        """ This method gets specific government office """
        if PoliticalParty.check_existence(self, "id", id, self.office_data) == False:
            abort(400)
        else:
            for i in self.office_data:
                if i.get("id") == id:
                    office_data = i
                    break


        return [office_data]
