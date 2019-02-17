import os

class Config(object):
    """ Our parent configuration class. """
    DEBUG = False
    SECRET = os.getenv('This is our lil secret')
    Database_Url = os.getenv('politico_db')


class DevelopmentConfig(Config):
    """ Configurations for Development. """
    DEBUG = True
    Database_Url = os.getenv('politico_db')


class TestingConfig(Config):
    """ Configurations for Testing. """
    TESTING = True
    DEBUG = True
    #Database_Url = os.getenv('politico_test_db')

# on heroku deployment
class ProductionConfig(Config):
    """ Configurations for Production. """
    DEBUG = False
    TESTING = False
    Database_Url = os.getenv('DATABASE_URL')


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
}
