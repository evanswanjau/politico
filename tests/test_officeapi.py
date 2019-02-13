""" These are all the Tests Concerned with Governmen Office API """
import simplejson as json
from tests.test_base import *
from tests.dummy_data import *


"""
Creating Government Office
"""
# test create government office url
def test_broken_gov_office_url(client):
    """ Tests whether the url returns the right response """
    response = create_new_item(client=client, url=broken_gov_url, data=office_data)
    assert response.status_code == 404

# test to create government office
def test_create_gov_office(client):
    """ Tests whether the api can create a government office """
    response = create_new_item(client=client, url=office_url, data=party_data)
    assert json.loads(response.data) == successful_office_creation_response
    assert response.status_code == 200


# test to validate empty data
def test_empty_office_data(client):
    """ Tests whether the api can create a government office """
    response = create_new_item(client=client, url=office_url, data=empty_office_data)
    assert json.loads(response.data) == already_exist_party_creation_error

"""
Get Government Offices
"""
# test to get all government office
def test_get_all_governmnt_offices(client):
    """ Test to get all government offices """
    response = get_item(client=client, url=get_all_government_offices_url)
    assert response.status_code == 200


# test to get a single political party
def test_get_government_office(client):
    """ Test to get a single government office """
    response = get_item(client=client, url=get_government_office_url)
    assert response.data == expected_single_office_data
    assert response.status_code == 200
