""" A storagefile for all dummy that should be used in tests """

"""
Create Political Party Data
"""

party_url = '/api/v1/create-political-party'
broken_party_url = '/api/v1/create-political-part'

party_data = {"party_id": 3, "party_name": "green party",
              "chairman": "hammer deltassds", "hqaddress": "76 J Street",
              "logoUrl": "political_party.img"}

empty_party_data = {"party_id": 3, "party_name": "",
              "chairman": "hammer deltassds", "hqaddress": "76 J Street",
              "logoUrl": "political_party.img"}
successful_party_creation_response = {"status": 200, "data": [{"id": 3, "name": "green party"}]}

already_exist_party_creation_error = {'error': 'Already Exists', 'status': 409}

"""
Edit Political Party Data
"""

edit_party_url = '/api/v1/edit-political-party/1'
edit_nonexisting_value = '/api/v1/edit-political-party/1000'
edit_invalid_value = '/api/v1/edit-political-party/t'

edit_party_data = {"party_id": 1, "party_name": "new updated party",
              "chairman": "glazer chimmy", "hqaddress": "90 Fifth Street",
              "logoUrl": "redparty.img"}
expected_edit_response_url_error = {'error': 'The requested URL was not found on the server.'
                                    '  If you entered the URL manually please check your spelling and try again.',
                                    'status': 404}
expected_edit_nonexisting_error_request = {'error': 'Invalid Request', 'status': 400}

successful_edit_reponse = {"status": 201, "data": [{"id": 1, "name": "new updated party"}]}


"""
Delete Political Party
"""
delete_party_url = '/api/v1/delete-political-party/1'
expected_deletion_message = {"status": 201, "message": ["deletion successful"]}


"""
Get Political Party
"""
get_all_political_parties_url = '/api/v1/political-parties'
get_political_party_url = '/api/v1/political-party/1'

expected_single_party_data = {"id": 1, "name": "blue party", "logoUrl":"blueparty.img"}


##########################################################################################
"""
Create Government Office Data
"""

office_url = '/api/v1/create-government-office'
broken_gov_url = '/api/v1/create-government-offi'

office_data = { "id": 3, "type": "state", "name": "prime minister"}
empty_office_data = { "id": 3, "type": "", "name": "prime minister"}
successful_office_creation_response = {"status": 200, "data": [{"id": 3, "type":"state",
                                       "name": "prime minister"}]}
already_exist_office_creation_error = {'error': 'Already Exists', 'status': 409}


"""
Get Government Office
"""
get_all_government_offices_url = '/api/v1/government-offices'
get_government_office_url = '/api/v1/government-office/1'

expected_single_office_data = {"data": [{"id": 1, "name": "president", "type": "state"}],"status": 200}
