""" Modules that will run on app initialization """

# method to drop existing tables
def drop_existing_tables():
    """ Drops all tables """
    tables_to_drop = [
        """ DROP TABLE IF EXISTS party """,
        """ DROP TABLE IF EXISTS users """,
        """ DROP TABLE IF EXISTS office """,
        """ DROP TABLE IF EXISTS candidates """,
        """ DROP TABLE IF EXISTS vote """,
        """ DROP TABLE IF EXISTS petition """
    ]

    return tables_to_drop

# method to create politico tables
def create_tables():
    """ create tables for our app """
    tables_to_create = [
        """
        CREATE TABLE party (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50) NOT NULL,
            hqAddress VARCHAR(50) NOT NULL,
            logoUrl VARCHAR(50) NOT NULL
        )
        """,
        """
        CREATE TABLE users (
            id SERIAL PRIMARY KEY,
            firstname VARCHAR(50) NOT NULL,
            secondname VARCHAR(50) NOT NULL,
            othername VARCHAR(50),
            email VARCHAR(50) NOT NULL,
            password VARCHAR(150) NOT NULL,
            phoneNumber VARCHAR (15) NOT NULL,
            passportUrl VARCHAR (50) NOT NULL,
            isAdmin BOOLEAN NOT NULL DEFAULT FALSE
        )
        """,
        """
        CREATE TABLE office (
            id SERIAL PRIMARY KEY,
            type VARCHAR(50) NOT NULL,
            name VARCHAR(50) NOT NULL
        )
        """,
        """
        CREATE TABLE candidates (
            id SERIAL PRIMARY KEY,
            office INTEGER NOT NULL,
            party INTEGER NOT NULL,
            candidate INTEGER NOT NULL
        )
        """,
        """
        CREATE TABLE vote (
            id SERIAL PRIMARY KEY,
            createdOn timestamp DEFAULT CURRENT_TIMESTAMP,
            createdBy INTEGER NOT NULL,
            office INTEGER NOT NULL,
            candidate INTEGER NOT NULL
        )
        """,
        """
        CREATE TABLE petition (
            id SERIAL PRIMARY KEY,
            createdOn timestamp DEFAULT CURRENT_TIMESTAMP,
            createdBy INTEGER NOT NULL,
            office INTEGER NOT NULL,
            body TEXT,
            evidence VARCHAR(100)
        )
        """]

    return tables_to_create


# method to create user admin
def create_admin():
    """ create admin user """
    # admin object
    # check whether admin exists
    # insert admin if not exists
