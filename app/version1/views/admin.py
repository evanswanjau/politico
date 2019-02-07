from flask import Flask, Blueprint, request, jsonify, make_response, json
from ..modules.party_module import PoliticalParty

bp = Blueprint('admin', __name__, url_prefix='/')

app = Flask(__name__)


party_list = [
    {
        "party_id": 1,
        "party_name": "blue party",
        "chairman": "hammer delta"
    },
    {
        "party_id": 2,
        "party_name": "red party",
        "chairman": "glazer chimmy"
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
    return make_response(jsonify({
        "political_parties": party_list,
        "status": "Ok"
    }), 200)
