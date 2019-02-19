""" The user module that is supposed to take care of all user methods and attributes """
import psycopg2
from psycopg2 import Error
from app.db.database import DBConnection

class UserModule():
    """ All user processes class """

    db = DBConnection()

    def __init__(self, data=None):
        self.data = data

    # signup user
    def signupUser(self):
        """ signup user """
        validated_object = self.data
        # add to db
        db.insert_data(validated_object)
        return [{"token": "#token", "user":validated_object}]


    # login user
    def loginUser(self):
        """ login user """
        validated_data = self.data

        query = """SELECT * FROM users WHERE email = {}""".format(validated_data["email"])
        user = db.fetch_single_item(query)
        if user:
            # validate password
        else:
            raise NotFoundError('user doesn\'t exist')
        return [{"token": "#token", "user":user}]


    # register candidate
    def registerCandidate(self, office_id):
        """ Express Candidate Interest """

        validated_data =  self.data

        # get user id
        userid_query = """ SELECT id FROM users WHERE email = {}"""
                       .format(validated_data['email'])
        user_id = fetch_single_item(userid_query)[0])

        # check whether user is a candidate
        candidate_query = """ SELECT candidate FROM candidates WHERE candidate = {}"""
                          .format(user_id)
        candidate = fetch_single_item(candidate_query)

        if candidate:
            raise ConflictError('user is already a candidate')
        else:
            # get political party id
            partyid_query = """ SELECT id FROM party WHERE name = {}"""
                           .format(validated_data['party_name'])
            party_id = fetch_single_item(userid_query)[0])

            # insert into db
            candidates = {"office":office_id, "party":party_id, "candidate":candidate}

            return {"office":office_id, "candidate":candidate}


    # vote

    # get political party results

    # petition
