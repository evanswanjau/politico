""" Modules that will run on app initialization """

# method to drop existing tables
def drop_existing_tables():
    """ Drops all tables """
    tables_to_drop = [
        """ DROP TABLE IF EXISTS party CASCADE""",
        """ DROP TABLE IF EXISTS users CASCADE""",
        """ DROP TABLE IF EXISTS office CASCADE""",
        """ DROP TABLE IF EXISTS candidates CASCADE""",
        """ DROP TABLE IF EXISTS vote CASCADE""",
        """ DROP TABLE IF EXISTS petition CASCADE"""
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
            candidate INTEGER NOT NULL,
            FOREIGN KEY (candidate) REFERENCES users(id) ON DELETE CASCADE
        )
        """,
        """
        CREATE TABLE vote (
            id SERIAL PRIMARY KEY,
            createdOn timestamp DEFAULT CURRENT_TIMESTAMP,
            createdBy INTEGER NOT NULL,
            office INTEGER NOT NULL,
            candidate INTEGER NOT NULL,
            FOREIGN KEY (createdBy) REFERENCES users (id) ON DELETE RESTRICT
        )
        """,
        """
        CREATE TABLE petition (
            id SERIAL PRIMARY KEY,
            createdOn timestamp DEFAULT CURRENT_TIMESTAMP,
            createdBy INTEGER NOT NULL,
            office INTEGER NOT NULL,
            body TEXT(100),
            evidence VARCHAR(100)
            FOREIGN KEY (office) REFERENCES vote (office) ON DELETE RESTRICT
        )
        """]

    return tables_to_create
