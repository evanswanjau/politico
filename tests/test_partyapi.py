from flask import jsonify
import simplejson as json

def test_hello_world(client):
    response = client.get('/')
    assert response.data == b'Hello, World!'


# test to create political party
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


# test to validate existing data
def test_validate_existing_data(client):
    """ Tests whether the api can validate existing data"""
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
    assert json.loads(response.data) == {'status': 409, 'error': 'Already Exists'}


# test to validate empty data
def test_validate_empty_data(client):
    """ Tests whether the api can create a calid request """
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
    assert json.loads(response.data) == {'status': 400, 'error': 'Invalid Request'}


# test to get all political parties
def test_all_political_parties(client):
    """ Test get all political parties """
    response = client.get('/api/v1/political-parties')
    assert response.status_code == 200


def test_get_specific_political_party(client):
    """ Test a single political party """
    response = client.get('/api/v1/political-party/1')
    assert response.status_code == 200
    response = client.get('/api/v1/political-party/t')
    assert response.status_code == 404
    response = client.get('/api/v1/political-party/78')
    assert response.status_code == 400
