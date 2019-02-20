""" The user module that is supposed to take care of all user methods and attributes """
import psycopg2, re, os
from app.db.database import DBConnection
from app.version2.modules.validation_module import DataValidation as dv
from ...error_handlers import *
DB_URL = os.getenv("DATABASE_URL")
db = DBConnection(DB_URL)
from flask_jwt_extended import (create_access_token)
from werkzeug.security import check_password_hash, generate_password_hash

class UserModule(dv):
    """ All user processes class """

    def __init__(self, data=None):
        self.data = data

    # signup user
    def signupUser(self):
        """ signup user """
        expected_fields = ['firstname', 'secondname', 'othername', 'email',
                           'password', 'phoneNumber', 'passportUrl']

        for field in expected_fields:
            dv.validateFields(field, self.data)

        # validate not empty and type
        for key in self.data:
            dv.validateEmpty(key, self.data[key])
            dv.validateType(self.data[key], str)

        # validate length
        dv.validate_length('phoneNumber', self.data['phoneNumber'], 10, 15)
        dv.validate_length('password', self.data['password'], 5, 50)

        # validate existence
        if dv.validateExistence('users', 'email', self.data['email']):
            raise ConflictError('email ' + self.data['email'] + ' already exists')

        if dv.validateExistence('users', 'phoneNumber', self.data['phoneNumber']):
            raise ConflictError('phoneNumber ' + self.data['phoneNumber'] + ' already exists')

        dv.validateExistence('users', 'phoneNumber', self.data['phoneNumber'])

        # insert to db
        data = self.data
        self.data["password"] = generate_password_hash(self.data["password"])
        db.insert_data('users', self.data)
        token = create_access_token(identity=self.data['email'])
        return [{"token": token, "user":self.data}]


    # login user
    def loginUser(self):
        """ login user """
        expected_fields = ['email', 'password']

        for field in expected_fields:
            dv.validateFields(field, self.data)

        # validate not empty and type
        for key in self.data:
            dv.validateEmpty(key, self.data[key])
            dv.validateType(self.data[key], str)

        # validate existence
        user_object = dv.validateExistence('users', 'email', self.data['email'])
        if user_object:
            if not check_password_hash(user_object["password"], self.data['password']):
                raise ForbiddenError('Incorrect password')
        else:
            raise NotFoundError('That acccount does not exist')

        token = create_access_token(identity=self.data['email'])
        return [{"token": token, "user":user_object}]


    # register candidate
    def registerCandidate(self, office_id):
        """ Express Candidate Interest """

        validated_data =  self.data

        # get user id
        userid_query = """ SELECT id FROM users
                       WHERE email = {}""".format(validated_data['email'])
        user_id = db.fetch_single_item(userid_query)[0]

        # check whether user is a candidate
        candidate_query = """ SELECT candidate FROM candidates
                          WHERE candidate = {}""".format(user_id)
        candidate = db.fetch_single_item(candidate_query)

        if candidate:
            raise ConflictError('user is already a candidate')
        else:
            # get political party id
            partyid_query = """ SELECT id FROM party
                            WHERE name = {}""".format(validated_data['party_name'])
            party_id = db.fetch_single_item(userid_query)[0]

            # insert into db
            candidates = {"office":office_id, "party":party_id, "candidate":candidate}
            db.insert_data('candidates', candidates)

            return {"office":office_id, "candidate":candidate}


    # vote
    def userVote(self):
        """ User Voting Process """
        validated_data = self.data

        userid_query = """ SELECT * FROM vote WHERE voter = {}
                       AND office = {}""".format(validated_data['voter'], validated_data['office'])
        vote_data = db.fetch_single_item(userid_query)[0]

        # check if user has already voted
        if vote_data:
            raise ConflictError('user has already voted')
        else:
            db.insert_data('vote', validated_data)
            return validated_data


    # get political office results
    def officeResults(self, office_id):
        """ Political Office Results """
        office_results = []

        candidates_query = """ SELECT candidate FROM vote WHERE office = {}\
                           GROUP BY candidate """.format(office_id)
        candidates = db.fetch_multiple_items(candidates_query)

        for candidate in candidates:
            votes_query = """ SELECT * FROM vote WHERE office = {}\
                          AND candidate = {} """.format(office_id, candidate[0])
            votes = len(db.fetch_multiple_items(votes_query))

            office_results.append({"office":office_id, "candidate":candidate[0],
                                   "result":votes})

        return office_results

    # petition
    def requestPetition(self):
        """ Request Partition Method """
        validated_data = self.data

        db.insert_data('petition', validated_data)
        return validated_data
