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


    def check_existence(self, key, value, data_list):
        """ Method That Checks Whether a Value Exists """
        return_value = False
        for i in data_list:
            if i.get(key) == value:
                return_value = True
                break

        return return_value


    def create_party(self):
        """ validate the political party data """

        # party id
        if not self.party_id:
            abort(400)
        else:
            if PoliticalParty.check_existence(self, "party_id", self.party_id, self.party_data):
                abort(409)
            else:
                party_id = self.party_id

        # party name
        if self.party_name == "":
            abort(400)
        else:
            if PoliticalParty.check_existence(self, "party_name", self.party_name, self.party_data):
                abort(409)
            else:
                party_name = self.party_name

        # chairman
        if not self.chairman:
            abort(400)
        else:
            if PoliticalParty.check_existence(self, "chairman", self.chairman, self.party_data):
                abort(409)
            else:
                chairman = self.chairman

        # hqaddress
        if not self.hqaddress:
            abort(400)
        else:
            if PoliticalParty.check_existence(self, "hqaddress", self.hqaddress, self.party_data):
                abort(409)
            else:
                hqaddress = self.hqaddress

        # logoUrl
        if not self.logoUrl:
            abort(400)
        else:
            if PoliticalParty.check_existence(self, "logoUrl", self.logoUrl, self.party_data):
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
        """ This method gets all political parties """
        political_parties = []
        party_data = self.party_data
        for i in party_data:
            new_dict = {"id":i["party_id"], "name":i["party_name"], "logoUrl":i["logoUrl"]}
            political_parties.append(new_dict)

        return political_parties


    def get_specific_political_party(self, id):
        """ This method gets specific political party """
        if PoliticalParty.check_existence(self, "party_id", id, self.party_data) == False:
            abort(400)
        else:
            for i in self.party_data:
                if i.get("party_id") == id:
                    party_data = i
                    break


        return [{"id":party_data["party_id"], "name":party_data["party_name"], "logoUrl":party_data["logoUrl"]}]


    def edit_political_party(self):
        if PoliticalParty.check_existence(self, "party_id", self.party_id, self.party_data) == False:
            abort(400)
        else:
            for i in self.party_data:
                if i.get("party_id") == self.party_id:
                    i["party_name"] = self.party_name
                    i["chairman"] = self.chairman
                    i["party_name"] = self.party_name
                    i["chairman"] = self.chairman
                    new_party_data = i
                    break

        return [{"id":self.party_id, "name":new_party_data["party_name"]}]


    def delete_political_party(self):
        if PoliticalParty.check_existence(self, "party_id", self.party_id, self.party_data) == False:
            abort(400)
        else:
            party_data = self.party_data
            for i in party_data:
                if i.get("party_id") == self.party_id:
                    party_data.remove(i)
                    break
            return ["deletion successful"]
