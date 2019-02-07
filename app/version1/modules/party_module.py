""" A class to handle the political party object """
from flask import jsonify, abort

class PoliticalParty():

    """ Methods and Attrinutes for PoliticalParty. """

    def __init__(self, party_id=None, party_name=None, chairman=None, hqaddress=None, logoUrl=None, party_data=None):
        self.party_id = party_id
        self.party_name = party_name
        self.chairman = chairman
        self.hqaddress = hqaddress
        self.logoUrl = logoUrl
        self.party_data = party_data


    def check_existence(self, key, value):
        """ Method That Checks Whether a Value Exists """
        return_value = False
        for i in self.party_data:
            if i.get(key) == value:
                return_value = True
                break

        return return_value


    def create_party(self):
        """ validate the political party data """
        errors = {}

        # party id
        if not self.party_id:
            abort(400)
        else:
            if PoliticalParty.check_existence(self, "party_id", self.party_id):
                abort(409)
            else:
                party_id = self.party_id

        # party name
        if self.party_name == "":
            abort(400)
        else:
            if PoliticalParty.check_existence(self, "party_name", self.party_name):
                abort(409)
            else:
                party_name = self.party_name

        # chairman
        if not self.chairman:
            abort(400)
        else:
            if PoliticalParty.check_existence(self, "chairman", self.chairman):
                abort(409)
            else:
                chairman = self.chairman

        # hqaddress
        if not self.hqaddress:
            abort(400)
        else:
            if PoliticalParty.check_existence(self, "hqaddress", self.hqaddress):
                abort(409)
            else:
                hqaddress = self.hqaddress

        # logoUrl
        if not self.logoUrl:
            abort(400)
        else:
            if PoliticalParty.check_existence(self, "logoUrl", self.logoUrl):
                abort(409)
            else:
                logoUrl = self.logoUrl


        return {
            "party_id": party_id,
            "party_name": party_name,
            "chairman": chairman,
            "hqaddress":hqaddress,
            "logoUrl":logoUrl
        }


    def get_all_political_parties(self):
        political_parties = []
        party_data = self.party_data
        for i in party_data:
            new_dict = {"id":i["party_id"], "name":i["party_name"], "logoUrl":i["logoUrl"]}
            political_parties.append(new_dict)

        return political_parties


    def get_specific_political_party(self, id):
        """ This method gets specific political party """
        if PoliticalParty.check_existence(self, "party_id", id) == False:
            abort(400)
        else:
            for i in self.party_data:
                if i.get("party_id") == id:
                    party_data = i
                    break


        return [{"id":party_data["party_id"], "name":party_data["party_name"], "logoUrl":party_data["logoUrl"]}]
