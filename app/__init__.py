""" This is the Application Initialization Method """
import os
from flask import Flask, make_response, jsonify
from instance.config import app_config
from .version1.views import admin

def create_app(test_config=None):
    """ Method to Build The APP """
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_pyfile('config.py')

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

    app.register_blueprint(admin.admin_bp)

    return app
