import psycopg2
from psycopg2 import Error

connection = psycopg2.connect(user = "postgres",
                              password = "pass123",
                              host = "127.0.0.1",
                              port = "5432",
                              database = "politico_db")

cursor = connection.cursor()

# method to create politico tables
def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
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
        """)
    connection = None
    try:
        # create table one by one
        for command in commands:
            cursor.execute(command)
        # close communication with the PostgreSQL database server
        cursor.close()
        # commit the changes
        connection.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()


if __name__ == '__main__':
    create_tables()
