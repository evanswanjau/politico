from flask.views import MethodView
from flask import make_response, jsonify, request
from ...modules.party_module import PoliticalParty
from ...modules.office_module import GovernmentOffice

party_list = [
    {
        "party_id": 1,
        "party_name": "blue party",
        "chairman": "hammer delta",
        "hqaddress":"474 Major Road",
        "logoUrl":"blueparty.img"
    },
    {
        "party_id": 2,
        "party_name": "red party",
        "chairman": "glazer chimmy",
        "hqaddress":"90 Fifth Street",
        "logoUrl":"redparty.img"
    }
]


office_list = [
    {
        "id": 1,
        "type": "state",
        "name": "president"
    },
    {
        "id": 2,
        "type": "state",
        "name": "vice president"
    }
]

# Political Party Class
class PartyAPI(MethodView):
    """ Party APIs Simplified Using Classes """
    def get(self, party_id):
        """ This will take care of getting political party data """
        political_party = PoliticalParty(party_data=party_list)
        if party_id is None:
            # return a list of all political parties
            political_parties = political_party.get_all_political_parties()

            return make_response(jsonify({
                "status": 200,
                "data": political_parties
                }), 200)
        else:
            single_political_party = PoliticalParty(party_data=party_list)
            political_party = single_political_party.get_specific_political_party(party_id)

            return make_response(jsonify({
                "status":200,
                "data": political_party
            }), 200)

    def post(self):
        """ Create Political Party """
        data = request.get_json()
        political_party = PoliticalParty(data['party_id'], data['party_name'],
                                         data['chairman'], data['hqaddress'],
                                         data['logoUrl'], party_list)

        new_party = political_party.create_party()
        party_list.append(new_party)
        return make_response(jsonify({
            "status": 200,
            "data": [{"id":new_party.get("party_id"), "name":new_party.get("party_name")}]
        }), 200)


    def patch(self, party_id):
        """ This will enable the update of a political party """
        data = request.get_json()
        edit_political_party = PoliticalParty(party_id=party_id,
                                              party_name=data['party_name'],
                                              party_data=party_list)
        updated_party = edit_political_party.edit_political_party()

        return make_response(jsonify({
            "status": 201,
            "data": [{"id":updated_party.get("party_id"), "name":updated_party.get("party_name")}]
        }), 201)


    def delete(self, party_id):
        """ This will enable the deletion of a political party """
        delete_political_party = PoliticalParty(party_id=party_id, party_data=party_list)
        message = delete_political_party.delete_political_party()
        return make_response(jsonify({
            "status": 201,
            "message": message,
        }), 201)


# Government Office Class
class OfficeAPI(MethodView):
    """ Office APIs Simplified Using Classes """
    def get(self, office_id):
        """ This will take care of getting political office data """
        political_office = GovernmentOffice(office_data=office_list)
        if office_id is None:
            # return a list of all political offices
            """ This will get all government offices """
            return make_response(jsonify({
                "status": 200,
                "data": office_list
            }), 200)
        else:
            office_data = political_office.get_specific_gov_office(office_id)
            return make_response(jsonify({
                "status":200,
                "data": office_data
            }), 200)

    def post(self):
        """ Create Government Office """
        data = request.get_json()
        office = GovernmentOffice(data['id'], data['type'], data['name'], office_list)
        new_office = office.create_office()

        office_list.append(new_office)
        return make_response(jsonify({
            "status": 200,
            "data": [new_office]
        }), 200)
