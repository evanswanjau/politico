import simplejson as json

# test to create government office
def test_create_government_office(client):
    """ Tests whether the api can create a government office"""
    party_data = {
        "id": 3,
        "type": "state",
        "name": "prime minister"
    }

    url = '/api/v1/create-gov-office'

    response = client.post(url, json=party_data)
    assert response.status_code == 200
    assert json.loads(response.data) == {"status": 200, "data": [{"id": 3, "type":"state", "name": "prime minister"}]}
