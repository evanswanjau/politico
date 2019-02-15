""" These are tests that support user API implementation in politico """
import simplejson as json

user_data = {"id": 3,
    "firstname": "kenneth", "lastname": "banner", "othername": "wilson",
     "email": "kenneth@gmail.com", "phonenumber": "0707000000", "passportUrl": "kennethbanner.jpg",
     "isAdmin": False
}

url = '/api/v2/auth/signup'

# tests to take care of signing up
def test_user_signup_url(client):
    """ test sign up url """
    response = client.post(url, data=json.dumps(user_data), content_type='application/json')
    assert response.status_code == 200
    assert response.status_code != 400

def test_wrong_sign_up_url(client):
    """ test incorrect url response """
    response = client.post('/api/v2/auth/signu')
    assert response.status_code == 404

def test_response_data(client):
    """ test data after account creation """
    response = client.post(url, data=json.dumps(user_data), content_type='application/json')
    created_data = json.loads(response.data)
    user_object = created_data["data"]["user"]
    assert user_object == {"id": 3, "firstname": "kenneth", "lastname": "banner",
                           "othername": "wilson", "email": "kenneth@gmail.com",
                           "phonenumber": "0707000000", "passportUrl": "kennethbanner.jpg",
                           "isAdmin": False}
def test_empty_data(client):
    user_data = {"id": 3,
        "firstname": "", "lastname": "banner", "othername": "wilson",
         "email": "kenneth@gmail.com", "phonenumber": "0707000000", "passportUrl": "kennethbanner.jpg",
         "isAdmin": False
    }
    assert response.status_code == 400


# tests to take care of signing in
user_data = {"email": "kenneth@gmail.com", "password":"password"}

url = '/api/v2/auth/login'

def test_user_login_url(client):
    """ test login url """
    response = client.post(url, data=json.dumps(user_data), content_type='application/json')
    assert response.status_code == 200
    assert response.status_code != 400

def test_wrong_login_url(client):
    """ test incorrect url response """
    response = client.post('/api/v2/auth/logi')
    assert response.status_code == 404

def test_response_data(client):
    """ test data after user login """
    response = client.post(url, data=json.dumps(user_data), content_type='application/json')
    created_data = json.loads(response.data)
    user_object = created_data["data"]["user"]
    assert user_object == {"id": 3, "firstname": "kenneth", "lastname": "banner",
                           "othername": "wilson", "email": "kenneth@gmail.com",
                           "phonenumber": "0707000000", "passportUrl": "kennethbanner.jpg",
                           "isAdmin": False}

def test_empty_data(client):
    user_data = {"email": "", "password":"password"}
    assert response.status_code == 400

# tests to take care of a user expressing interest
""" Test user expressing Interest """

url = '/api/v2/office/1/register'

register_data = {"office_id":2, "user_id":3}

def test_user_express_interest_url(client):
    """ test express interest url """
    response = client.post(url, data=json.dumps(register_data), content_type='application/json')
    assert response.status_code == 200
    assert response.status_code != 400

def test_wrong_express_interest_url(client):
    """ test incorrect url response """
    response = client.post('/api/v2/office/1/registe')
    assert response.status_code == 404

def test_response_data(client):
    """ test data after user login """
    response = client.post(url, data=json.dumps(register_data), content_type='application/json')
    assert json.loads(response.data) == {"status":200, "data":{"office":2, "user":3}}


# tests to take care of voting
url = '/api/v2/votes'

voting_data = {"office_data":3, "candidate_id":4, "user_id":3}

def test_user_voting_url(client):
    """ test express interest url """
    response = client.post(url, data=json.dumps(voting_data), content_type='application/json')
    assert response.status_code == 200
    assert response.status_code != 400

def test_wrong_voting_url(client):
    """ test incorrect url response """
    response = client.post('/api/v2/vot')
    assert response.status_code == 404

def test_response_data(client):
    """ test data after user login """
    response = client.post(url, data=json.dumps(voting_data), content_type='application/json')
    assert json.loads(response.data) == {"status":200, "data":{"office":2, "candidate":2, "voter":3}}


# tests to take care of the election results
url = '/api/v2/office/1/results'

def test_results_url(client):
    """ test results url """
    response = client.get(url)
    assert response.status_code == 200
    assert response.status_code != 400

def test_wrong_results_url(client):
    """ test incorrect url response """
    response = client.get('/api/v2/office/1/result')
    assert response.status_code == 404


# tests to take care of creating a petition
""" Test user petitioning """

url = '/api/v2/petitions'

def test_petitions_url(client):
    """ test results url """
    response = client.get(url)
    assert response.status_code == 200
    assert response.status_code != 400

def test_wrong_results_url(client):
    """ test incorrect url response """
    response = client.get('/api/v2/petitio')
    assert response.status_code == 404
