[![Build Status](https://travis-ci.com/evanswanjau/politico.svg?branch=develop)](https://travis-ci.com/evanswanjau/politico) [![Coverage Status](https://coveralls.io/repos/github/evanswanjau/politico/badge.svg?branch=develop)](https://coveralls.io/github/evanswanjau/politico?branch=develop) [![Maintainability](https://api.codeclimate.com/v1/badges/b2846981cb310794c2c6/maintainability)](https://codeclimate.com/github/evanswanjau/politico/maintainability)


# politico
An simple online voting application.

## Description
An online voting system that enables user (voters/politicians) to vote. One is able to become a user by simply creating an account. Then the user can choose to be a politician by expressing interest. THe administrator is in control of political party and government creation and maintainance.

## Politico Endopints

| Request  | Endpoint | Description |
| ------------- | ------------- | ------------- |
| POST | /api/v1/create-political-party  | Creates a political party  |
| POST | /api/v1/create-government-office  | Creates a government office  |
| GET | /api/v1/political-parties  | Gets all political parties  |
| GET | /api/v1/political-party/<int:party_id> | Gets a specific political party  |
| GET | /api/v1/government-offices  | Gets all government offices  |
| GET | /api/v1/government-office/<int:office_id> | Gets a specific government office  |
| PATCH | /api/v1/edit-political-party/<int:party_id> | Edits a political party  |
| DELETE | /api/v1/delete-political-party/<int:party_id>  | Deletes a political party  |

## Links
* **PIVOTAL TRACKER:** https://www.pivotaltracker.com/n/projects/2241809
* **UI:** https://evanswanjau.github.io/politico/UI/
* **HEROKU:** https://politico-by-evanswanjau.herokuapp.com/

### Credits
Andela Bootcamp


###Author
Evans Wanjau Muchiri
