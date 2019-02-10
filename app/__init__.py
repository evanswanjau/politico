""" This is the Application Initialization Method """
import os
from flask import Flask, make_response, jsonify

def create_app(test_config=None):
    """ Method to Build The APP """
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('conftest.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    @app.errorhandler(400)
    @app.errorhandler(403)
    @app.errorhandler(404)
    @app.errorhandler(405)
    @app.errorhandler(409)
    def http_error_handler(error):
        return make_response(jsonify({'status': error.code, 'error': error.description}), error.code)

    # a simple page that says hello
    @app.route('/')
    def hello():
        return 'Hello, World!'

    from .version1.views import admin
    app.register_blueprint(admin.BP)

    return app
