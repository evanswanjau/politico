[![Build Status](https://travis-ci.com/evanswanjau/politico.svg?branch=develop)](https://travis-ci.com/evanswanjau/politico) [![Coverage Status](https://coveralls.io/repos/github/evanswanjau/politico/badge.png?branch=develop)](https://coveralls.io/github/evanswanjau/politico?branch=develop) [![Maintainability](https://api.codeclimate.com/v1/badges/b2846981cb310794c2c6/maintainability)](https://codeclimate.com/github/evanswanjau/politico/maintainability)


# politico
An simple online voting application.

## Description
An online voting system that enables user (voters/politicians) to vote. One is able to become a user by simply creating an account. Then the user can choose to be a politician by expressing interest. THe administrator is in control of political party and government creation and maintenance.

#Installation
This is the project's installation for a linux machine

clone the repository to your local machine
git clone https://github.com/evanswanjau/politico.git

Install virtual environment
python3 -m venv venv

Create a .env file; copy and save the code below.
```
. venv/bin/activate
set FLASK_APP="app"
set APP_SETTINGS="development"
set FLASK_ENV="development"
set DATABASE_URL="postgresql://postgres:pass123@127.0.0.1/politico_db"
TEST_DATABASE_URL="postgresql://postgres:pass123@127.0.0.1/politico_tets_db"
```

On your terminal, run source .env to activate the virtual environment

`pip install -r requirements.txt` to install the necessary packages for this application.

Ensure that you have *postgreSql* Installed

Then run the application by executing *flask run*

## Politico Endpoints

| Request  | Endpoint | Description |
| ------------- | ------------- | ------------- |
| POST | /api/v2/auth/signup | Signup a new user  |
| POST | /api/v2/auth/login  | Logs in an already existing user  |
| POST | /api/v2/parties  | Creates a political party  |
| GET | /api/v2/parties/  | Gets all political parties  |
| GET | /api/v2/parties/<int:party_id> | Gets a specific political party  |
| PATCH | /api/v2/parties/<int:party_id>/name | Edits the name of a political party  |
| DELETE | /api/v2/parties/<int:party_id>/  | Deletes a political party  |
| POST | /api/v2/offices  | Creates a government office  |
| GET | /api/v2/offices  | Gets all government offices  |
| GET | /api/v2/offices/<int:office_id> | Gets a specific government office  |
| POST | /api/v2/office/<int:office_id>/register/  | Registers a Candidate  |
| POST | /api/v2/votes/  | Votes for a candidate |
| GET | /api/v2/offices/<int:office_id>/result  | Gets results for a specific office |
| POST | /api/v2/petition | Creates a petition for a candidates result  |


## Links
* **PIVOTAL TRACKER:** https://www.pivotaltracker.com/n/projects/2241809
* **UI:** https://evanswanjau.github.io/politico/UI/
* **HEROKU:** https://politico-by-evanswanjau.herokuapp.com/

### Credits
Andela Bootcamp


### Author
Evans Wanjau Muchiri
