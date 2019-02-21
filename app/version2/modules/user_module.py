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
        item = dv.validateExistence('users', 'email', self.data['email'])

        user_object = {"id":item[0], "firstname":item[1], "secondname":item[2],
        "othername":item[3], "email":item[4], "password":item[5], "hqAddress":item[6],
        "passportUrl":item[7], "isAdmin":item[8]}

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

        expected_fields = ['party', 'candidate']

        for field in expected_fields:
            dv.validateFields(field, self.data)

        # validate not empty and type
        for key in self.data:
            dv.validateEmpty(key, self.data[key])
            dv.validateType(self.data[key], int)

        user_id = dv.validateExistence('users', 'id', self.data['candidate'])

        if not user_id:
            raise BaseError(400, c_message="Candidate is not a registered user")
        else:
            # validate existence
            candidate_object = dv.validateExistence('candidates', 'candidate', self.data['candidate'])
            if not candidate_object:
                self.data['office'] = office_id
                db.insert_data('candidates', self.data)
            else:
                raise ConflictError('user is already a candidate')

        return {"office":self.data["office"], "user":self.data["candidate"]}


    # vote
    def userVote(self):
        """ User Voting Process """

        expected_fields = ['createdBy', 'office', 'candidate']

        for field in expected_fields:
            dv.validateFields(field, self.data)

        # validate not empty and type
        for key in self.data:
            dv.validateEmpty(key, self.data[key])
            dv.validateType(self.data[key], int)


        user_id = dv.validateExistence('users', 'id', self.data['candidate'])

        if not user_id:
            raise BaseError(400, c_message="Candidate is not a registered user")
        else:
            user_vote_query = """ SELECT * FROM vote WHERE office = {}
                              AND createdBy = {} """.format(self.data['office'], self.data['createdBy'])

            user = db.fetch_single_item(user_vote_query)
            if user:
                raise ConflictError('user has already voted')
            else:
                validated_data = {"office":self.data['office'], "candidate":self.data['candidate'],
                        "createdBy": self.data['createdBy']}
                db.insert_data('vote', validated_data)

        return {"office":self.data['office'], "candidate":self.data['candidate'],
                "voter": self.data['createdBy']}


    # get political office results
    def officeResults(self, office_id):
        """ Political Office Results """
        office_results = []

        candidates_query = """ SELECT candidate FROM vote WHERE office = {}
                           GROUP BY candidate """.format(office_id)
        candidates = db.fetch_multiple_items(candidates_query)

        for candidate in candidates:
            votes_query = """ SELECT * FROM vote WHERE office = {}
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
