import os

class Config(object):
    """ Our parent configuration class. """
    DEBUG = False
    SECRET = os.getenv('This is our lil secret')


class DevelopmentConfig(Config):
    """ Configurations for Development. """
    DEBUG = True


class TestingConfig(Config):
    """ Configurations for Testing. """
    TESTING = True
    DEBUG = True


class ProductionConfig(Config):
    """ Configurations for Production. """
    DEBUG = False
    TESTING = False


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
}
