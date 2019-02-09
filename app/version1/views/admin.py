""" This is all the functions the admin will take care of """
from flask import Flask, Blueprint, request, jsonify, make_response
from ..modules.party_module import PoliticalParty
from ..modules.office_module import GovernmentOffice

BP = Blueprint('admin', __name__, url_prefix='/api/v1/')

app = Flask(__name__)


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


# create political party endpoint
@BP.route('create-political-party', methods=['POST'])
def create_political_party():
    """ Create political party emdpoint """
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


# view all political parties
@BP.route('political-parties', methods=['GET'])
def political_parties():
    """ This will get all political parties """
    political_parties = PoliticalParty(party_data=party_list)

    political_parties = political_parties.get_all_political_parties()

    return make_response(jsonify({
        "status": 200,
        "data": political_parties
    }), 200)


# get a specific political party
@BP.route('political-party/<int:party_id>', methods=['GET'])
def get_political_party(party_id):
    """ Get a specific political party """

    single_political_party = PoliticalParty(party_data=party_list)

    party_info = single_political_party.get_specific_political_party(party_id)

    return make_response(jsonify({
        "status":200,
        "data": party_info
    }), 200)


# edit a specific political party
@BP.route('edit-political-party/<int:party_id>', methods=['PATCH'])
def edit_political_party(party_id):
    """ This will enable the update of a political party """
    data = request.get_json()

    edit_political_party = PoliticalParty(party_id, data['name'],
                                          data['chairman'], data['hqaddress'],
                                          data['logoUrl'], party_list)

    updated_party = edit_political_party.edit_political_party()

    return make_response(jsonify({
        "status": 201,
        "data": updated_party
    }), 201)


# delete a specific political party
@BP.route('delete-political-party/<int:party_id>', methods=['DELETE'])
def delete_political_party(party_id):
    """ This will enable the deletion of a political party """
    delete_political_party = PoliticalParty(party_id=party_id, party_data=party_list)

    message = delete_political_party.delete_political_party()

    return make_response(jsonify({
        "status": 201,
        "message": message,
    }), 201)



#------------------------------------------------------
# Government Office API's
#------------------------------------------------------

# create a government Office API
@BP.route('create-gov-office', methods=['POST'])
def create_government_office():

    """ Create government office endpoint """

    data = request.get_json()

    office = GovernmentOffice(data['id'], data['type'], data['name'], office_list)

    new_office = office.create_office()

    office_list.append(new_office)

    return make_response(jsonify({
        "status": 200,
        "data": [new_office]
    }), 200)


# view all government offices
@BP.route('government-offices', methods=['GET'])
def government_offices():
    """ This will get all government offices """
    return make_response(jsonify({
        "status": 200,
        "data": office_list
    }), 200)


# get a specific government office
@BP.route('government-office/<int:office_id>', methods=['GET'])
def get_government_office(office_id):
    """ Get a specific government office """

    single_office = GovernmentOffice(office_data=office_list)

    office_info = single_office.get_specific_government_office(office_id)

    return make_response(jsonify({
        "status":200,
        "data": office_info
    }), 200)
