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
        user = db.fetch_single_item(query)[0]
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
        user_id = db.fetch_single_item(userid_query)[0]

        # check whether user is a candidate
        candidate_query = """ SELECT candidate FROM candidates WHERE candidate = {}"""
                          .format(user_id)
        candidate = db.fetch_single_item(candidate_query)

        if candidate:
            raise ConflictError('user is already a candidate')
        else:
            # get political party id
            partyid_query = """ SELECT id FROM party WHERE name = {}"""
                           .format(validated_data['party_name'])
            party_id = db.fetch_single_item(userid_query)[0]

            # insert into db
            candidates = {"office":office_id, "party":party_id, "candidate":candidate}
            db.insert_data('candidates', candidates)

            return {"office":office_id, "candidate":candidate}


    # vote
    def userVote(self):
        """ User Voting Process """
        validated_data = self.data

        userid_query = """ SELECT * FROM vote WHERE voter = {} AND office = {}"""
                       .format(validated_data['voter'], validated_data['office'])
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
