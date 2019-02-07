from flask import Flask, Blueprint, request, jsonify, make_response, json
from ..modules.party_module import PoliticalParty

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


# create political party endpoint
@bp.route('/api/v1/create-political-party', methods=['POST'])
def create_political_party():
    """ Create political party emdpoint """
    data = request.get_json()

    id = data['id']
    name = data['name']
    chairman = data['chairman']
    hqaddress = data['hqaddress']
    logoUrl = data['logoUrl']

    POLITICAL_PARTY = PoliticalParty(data['id'], data['name'], data['chairman'], data['hqaddress'], data['logoUrl'], party_list)

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
