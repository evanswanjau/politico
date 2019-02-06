from flask import jsonify
import simplejson as json

def test_hello_world(client):
    response = client.get('/')
    assert response.data == b'Hello, World!'


def test_create_political_party(client):
    """ Tests whether the api can create a political party """
    party_data = {
	           "id": 3,
               "name": "green party",
               "chairman": "hammer deltassds",
               "hqaddress": "76 J Street",
               "logoUrl": "political_party.img"
        }

    url = '/api/v1/create-political-party'

    response = client.post(url, json=party_data)
    assert response.status_code == 200
    assert json.loads(response.data) == {"data": [{"id": 3,"name": "green party"}],"status": 200}


def test_validate_existing_data(client):
    party_data = {
	           "id": 1,
               "name": "green party",
               "chairman": "hammer deltas",
               "hqaddress": "76 J Street",
               "logoUrl": "political_party.img"
        }

    url = '/api/v1/create-political-party'

    response = client.post(url, json=party_data)
    assert response.status_code == 409
    assert json.loads(response.data) == {'error': 'Already Exists'}


def test_validate_empty_data(client):
    party_data = {
	           "id": 5,
               "name": "",
               "chairman": "hammer delta",
               "hqaddress": "76 J Street",
               "logoUrl": "political_party.img"
        }

    url = '/api/v1/create-political-party'

    response = client.post(url, json=party_data)
    assert response.status_code == 400
    assert json.loads(response.data) == {'error': 'Invalid Request'}
