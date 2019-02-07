from flask import Flask, Blueprint, request, jsonify, make_response, json
from ..modules.party_module import PoliticalParty
from ..modules.office_module import GovernmentOffice

bp = Blueprint('admin', __name__, url_prefix='/')

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
@bp.route('/api/v1/create-political-party', methods=['POST'])
def create_political_party():
    """ Create political party emdpoint """
    data = request.get_json()

    POLITICAL_PARTY = PoliticalParty(data['party_id'], data['party_name'], data['chairman'], data['hqaddress'], data['logoUrl'], party_list)

    new_party = POLITICAL_PARTY.create_party()

    party_list.append(new_party)

    return make_response(jsonify({
        "status": 200,
        "data": [{"id":new_party.get("party_id"), "name":new_party.get("party_name")}]
    }), 200)


# view all political parties
@bp.route('/api/v1/political-parties', methods=['GET'])
def political_parties():

    POLITICAL_PARTIES = PoliticalParty(party_data=party_list)

    political_parties = POLITICAL_PARTIES.get_all_political_parties()

    return make_response(jsonify({
        "status": 200,
        "data": political_parties
    }), 200)


# get a specific political party
@bp.route('/api/v1/political-party/<int:party_id>', methods=['GET'])
def get_political_party(party_id):
    """ Get a specific political party """

    SINGLE_POLITICAL_PARTY = PoliticalParty(party_data=party_list)

    party_info = SINGLE_POLITICAL_PARTY.get_specific_political_party(party_id)

    return make_response(jsonify({
        "status":200,
        "data": party_info
    }), 200)


# edit a specific political party
@bp.route('/api/v1/edit-political-party/<int:party_id>', methods=['PATCH'])
def edit_political_party(party_id):
    """ This will enable the update of a political party """
    data = request.get_json()

    EDIT_POLITICAL_PARTY = PoliticalParty(party_id, data['name'], data['chairman'], data['hqaddress'], data['logoUrl'], party_list)

    updated_party = EDIT_POLITICAL_PARTY.edit_political_party()

    return make_response(jsonify({
        "status": 201,
        "data": updated_party
    }), 201)


# delete a specific political party
@bp.route('/api/v1/delete-political-party/<int:party_id>', methods=['DELETE'])
def delete_political_party(party_id):

    DELETE_POLITICAL_PARTY = PoliticalParty(party_id=party_id, party_data=party_list)

    message = DELETE_POLITICAL_PARTY.delete_political_party()

    return make_response(jsonify({
        "status": 201,
        "message": message,
    }), 201)



#------------------------------------------------------
# Government Office API's
#------------------------------------------------------

# create a government Office API
@bp.route('/api/v1/create-gov-office', methods=['POST'])
def create_government_office():

    """ Create government office endpoint """

    data = request.get_json()

    OFFICE = GovernmentOffice(data['id'], data['type'], data['name'], office_list)

    new_office = OFFICE.create_office()

    office_list.append(new_office)

    return make_response(jsonify({
        "status": 200,
        "data": [new_office]
    }), 200)
