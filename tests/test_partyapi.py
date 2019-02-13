""" These are all the Tests Concerned with Political Parties API """
import simplejson as json
from tests.test_base import *
from tests.dummy_data import *


"""
Creating Political Party
"""
# test create political party url
def test_broken_political_party_url(client):
    """ Tests whether the url returns the right response """
    response = create_new_item(client=client, url=broken_party_url, data=party_data)
    assert response.status_code == 404

# test to create political party
def test_create_political_party(client):
    """ Tests whether the api can create a political party """
    response = create_new_item(client=client, url=party_url, data=party_data)
    assert json.loads(response.data) == successful_party_creation_response
    assert response.status_code == 200


# test to validate empty data
def test_empty_party_data(client):
    """ Tests whether the api can create a political party """
    response = create_new_item(client=client, url=party_url, data=empty_party_data)
    assert json.loads(response.data) == already_exist_party_creation_error


"""
Edting Political Party
"""
# test to edit political party
def test_edit_political_party(client):
    """ Tests whether the api can edit a political party """
    response = edit_item(client=client, url=edit_party_url, data=edit_party_data)
    assert json.loads(response.data) == successful_edit_reponse
    assert response.status_code == 201

# test to validate data that doesn't exists
def test_nonexisting_data(client):
    """ Test a value that does not exist """
    response = edit_item(client=client, url=edit_nonexisting_value, data=edit_party_data)
    assert json.loads(response.data) == expected_edit_nonexisting_error_request

# test to validate type of data value requested
def test_edit_party_value(client):
    """ Tests an incorrect value """
    response = edit_item(client=client, url=edit_invalid_value, data=edit_party_data)
    assert json.loads(response.data) == expected_edit_response_url_error


"""
Delete Political Party
"""
# test to delete political party
def test_delete_political_party(client):
    """ Test deletion of political party """
    response = delete_item(client=client, url=delete_party_url)
    assert json.loads(response.data) == expected_deletion_message
    assert response.status_code == 201


"""
Get PoliticalParties
"""
# test to get all political parties
def test_get_all_political_parties(client):
    """ Test to get all political parties """
    response = get_item(client=client, url=get_all_political_parties_url)
    assert response.status_code == 200


# test to get a single political party
def test_get_political_party(client):
    """ Test to get a single political party """
    response = get_item(client=client, url=get_political_party_url)
    assert response.data == expected_single_party_data
    assert response.status_code == 200
