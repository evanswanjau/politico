""" The user module that is supposed to take care of all user methods and attributes """
import psycopg2

class User():
    """ All user processes class """

    # signup user
    def signupUser(data):
        # validate all data
        fname = data["fname"]
        sname = data["sname"]
        oname = data["oname"]
        email = data["email"]
        pNumber = data["pNumber"]
        passportUrl = data["passportUrl"]
        insert_user = "INSERT INTO users(firstname, secondname, othername, email,
                                         phoneNumber, passportUrl)\
                       VALUES (fname, sname, oname, email, pNumber, passportUrl)"
        cursor.execute(insert_user)
        cursor.close()
        connection.commit()
        connection.close()
        return data

    # login user

    # express interest

    # vote

    # get political party results

    # petition
