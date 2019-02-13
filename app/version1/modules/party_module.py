""" A class to handle the political party object """
from flask import abort

class PoliticalParty():

    """ Methods and Attrinutes for PoliticalParty. """

    def __init__(self, party_id=None, party_name=None, chairman=None,
                 hqaddress=None, logo_url=None, party_data=None):
        self.party_id = party_id
        self.party_name = party_name
        self.chairman = chairman
        self.hqaddress = hqaddress
        self.logo_url = logo_url
        self.party_data = party_data

    def check_existence(self, key, value, data_list):
        """ Method That Checks Whether a Value Exists """
        return_value = False
        for i in data_list:
            if i.get(key) == value:
                return_value = True
                break

        return return_value


    def check_empty_and_check_existence(self, key, value, data):
        """ This method validates empty data or non existing data """
        if not value or value == "":
            abort(400, 'Invalid Request')
        elif PoliticalParty.check_existence(self, key, value, data):
            abort(409, 'Already Exists')
        else:
            return value


    def create_party(self):
        """ validate the political party data """

        # party id
        party_id = PoliticalParty.check_empty_and_check_existence(self, "party_id",
                                                                  self.party_id, self.party_data)
        # party name
        party_name = PoliticalParty.check_empty_and_check_existence(self, "party_name",
                                                                    self.party_name, self.party_data)
        # chairman
        chairman = PoliticalParty.check_empty_and_check_existence(self, "chairman",
                                                                  self.chairman, self.party_data)
        # hqaddress
        hqaddress = PoliticalParty.check_empty_and_check_existence(self, "hqaddress",
                                                                   self.hqaddress, self.party_data)
        # logoUrl
        logo_url = PoliticalParty.check_empty_and_check_existence(self, "logoUrl",
                                                                  self.logo_url, self.party_data)


        return {
            "party_id": party_id,
            "party_name": party_name,
            "chairman": chairman,
            "hqaddress":hqaddress,
            "logoUrl":logo_url
        }


    def get_all_political_parties(self):
        """ This method gets all political parties """
        political_parties = []
        party_data = self.party_data
        for i in party_data:
            new_dict = {"id":i["party_id"], "name":i["party_name"], "logoUrl":i["logoUrl"]}
            political_parties.append(new_dict)

        return political_parties


    def get_specific_political_party(self, party_id):
        """ This method gets specific political party """
        if not PoliticalParty.check_existence(self, "party_id", party_id, self.party_data):
            abort(400, 'Invalid Request')
        else:
            for i in self.party_data:
                if i.get("party_id") == party_id:
                    party_data = i
                    break

        return [{"id":party_data["party_id"], "name":party_data["party_name"],
                 "logoUrl":party_data["logoUrl"]}]


    def edit_political_party(self):
        """ This method edits a specific political party """
        if not PoliticalParty.check_existence(self, "party_id", self.party_id,
                                              self.party_data):
            abort(400, 'Invalid Request')
        else:
            for i in self.party_data:
                if i.get("party_id") == self.party_id:
                    i["party_name"] = self.party_name
                    updated_party = i
                    break

        return updated_party


    def delete_political_party(self):
        """ This method deletes a specific political party """
        if not PoliticalParty.check_existence(self, "party_id", self.party_id,
                                              self.party_data):
            abort(400, 'Invalid Request')
        else:
            party_data = self.party_data
            for i in party_data:
                if i.get("party_id") == self.party_id:
                    party_data.remove(i)
                    break

        return ["deletion successful"]
