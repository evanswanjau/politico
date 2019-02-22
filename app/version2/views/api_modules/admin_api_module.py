""" User implementation module """
from flask.views import MethodView
from flask import make_response, jsonify, request
from ...modules.party_module import PoliticalParty
from ...modules.office_module import GovernmentOffice

# Political Party Class
class PartyAPI(MethodView):
    """ Party APIs Simplified Using Classes """
    def get(self, party_id):
        """ This will take care of getting political party data """
        party = PoliticalParty()
        if party_id is None:
            # return a list of all political parties
            parties = party.get_all_political_parties()

            return make_response(jsonify({
                "status": 200,
                "data": parties
                }), 200)
        else:
            s_party = party.get_specific_political_party(party_id)

            return make_response(jsonify({
                "status":200,
                "data": s_party
            }), 200)

    def post(self):
        """ Create Political Party """
        data = request.get_json()
        party = PoliticalParty(data)
        new_party = party.create_party()
        return make_response(jsonify({
            "status": 201,
            "data": new_party
        }), 201)


    def patch(self, party_id):
        """ This will enable the update of a political party """
        data = request.get_json()
        party = PoliticalParty(data)
        u_party = party.edit_political_party(party_id)

        return make_response(jsonify({
            "status": 201,
            "data": u_party
        }), 201)


    def delete(self, party_id):
        """ This will enable the deletion of a political party """
        party = PoliticalParty()
        message = party.delete_political_party(party_id)
        return make_response(jsonify({
            "status": 200,
            "message": message,
        }), 200)


# Government Office Class
class OfficeAPI(MethodView):
    """ Office APIs Simplified Using Classes """
    def get(self, office_id):
        """ This will take care of getting political office data """
        office = GovernmentOffice()
        if office_id is None:
            # return a list of all political offices
            """ This will get all government offices """
            data = office.get_all_government_offices()
            return make_response(jsonify({
                "status": 200,
                "data": data
            }), 200)
        else:
            data = office.get_specific_gov_office(office_id)
            return make_response(jsonify({
                "status":200,
                "data": data
            }), 200)

    def post(self):
        """ Create Government Office """
        data = request.get_json()
        office = GovernmentOffice(data)
        new_office = office.create_office()

        return make_response(jsonify({
            "status": 201,
            "data": new_office
        }), 201)
