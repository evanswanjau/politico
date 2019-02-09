""" These are all the Tests Concerned with Political Parties API """
import simplejson as json

def test_hello_world(client):
    """ Simple Test for Home Page """
    response = client.get('/')
    assert response.data == b'Hello, World!'


# test to create political party
def test_create_political_party(client):
    """ Tests whether the api can create a political party """
    party_data = {"party_id": 3, "party_name": "green party",
                  "chairman": "hammer deltassds", "hqaddress": "76 J Street",
                  "logoUrl": "political_party.img"}

    url = '/api/v1/create-political-party'

    response = client.post(url, data=json.dumps(party_data), content_type='application/json')
    assert response.status_code == 200
    assert json.loads(response.data) == {"status": 200, "data": [{"id": 3, "name": "green party"}]}


# test to validate existing data
def test_validate_existing_data(client):
    """ Tests whether the api can validate existing data"""
    party_data = {"party_id": 1, "party_name": "green party",
                  "chairman": "hammer deltassds", "hqaddress": "76 J Street",
                  "logoUrl": "political_party.img"}

    url = '/api/v1/create-political-party'

    response = client.post(url, data=json.dumps(party_data), content_type='application/json')
    assert response.status_code == 409
    assert json.loads(response.data) == {'status': 409, 'error': 'Already Exists'}


# test to validate empty data
def test_validate_empty_data(client):
    """ Tests whether the api can create an invalid request """
    party_data = {"party_id": 5, "party_name": "",
                  "chairman": "hammer deltassds", "hqaddress": "76 J Street",
                  "logoUrl": "political_party.img"}

    url = '/api/v1/create-political-party'

    response = client.post(url, data=json.dumps(party_data), content_type='application/json')
    assert response.status_code == 400
    assert json.loads(response.data) == {'status': 400, 'error': 'Invalid Request'}


# test to get all political parties
def test_all_political_parties(client):
    """ Test get all political parties """
    response = client.get('/api/v1/political-parties')
    assert response.status_code == 200


# test to get a specific political party
def test_get_specific_political_party(client):
    """ Test a single political party """
    response = client.get('/api/v1/political-party/1')
    assert response.status_code == 200
    response = client.get('/api/v1/political-party/t')
    assert response.status_code == 404
    response = client.get('/api/v1/political-party/78')
    assert response.status_code == 400


# test to edit a political party
def test_edit_political_party(client):
    """ Test the editing of a political party """
    party_data = {"id": 3, "name": "new updated party",
                  "chairman": "hammer deltassds", "hqaddress": "76 J Street",
                  "logoUrl": "political_party.img"}

    url = '/api/v1/edit-political-party/1'

    response = client.patch(url, data=json.dumps(party_data), content_type='application/json')
    assert response.status_code == 201
    assert json.loads(response.data) == {"status": 201,
                                         "data": [{"id": 1, "name": "new updated party"}]}


# test to delete a political party
def test_delete_political_party(client):
    """ Test deletion of a political party """
    response = client.delete('/api/v1/delete-political-party/1')
    assert response.status_code == 201
    assert json.loads(response.data) == {"status": 201, "message": ["deletion successful"]}
    response = client.delete('/api/v1/delete-political-party/78')
    assert response.status_code == 400
