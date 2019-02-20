import os

class Config(object):
    """ Our parent configuration class. """
    DEBUG = False
    SECRET = os.getenv('This is our lil secret')
    DB_URL = os.getenv('politico_db')


class DevelopmentConfig(Config):
    """ Configurations for Development. """
    DEBUG = True
    DB_URL = os.getenv('politico_db')


class TestingConfig(Config):
    """ Configurations for Testing. """
    TESTING = True
    DEBUG = True
    DB_URL = os.getenv('politico_test_db')

# on heroku deployment
class ProductionConfig(Config):
    """ Configurations for Production. """
    DEBUG = False
    TESTING = False
    DB_URL = os.getenv('DATABASE_URL')


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
}
