""" This is the Application Initialization Method """
import os
from flask import Flask, make_response, jsonify
from instance.config import app_config
from app.error_handlers import *

def create_app(test_config=None):
    """ Method to Build The APP """
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_pyfile('config.py')

    @app.errorhandler(ConflictError)
    @app.errorhandler(ValidationError)
    @app.errorhandler(ConflictError)
    @app.errorhandler(PermissionError)
    @app.errorhandler(MethodError)
    @app.errorhandler(ServerError)
    def handle_error(error):
        return make_response(jsonify(error.to_dict()))

    # This will catch any uncaught http error
    @app.errorhandler(Exception)
    def exceptional_error(error):
        return make_response(jsonify({"status":error.code, "message":error.description}))

    # a simple page that says hello
    @app.route('/')
    def hello():
        return 'Hello, World!'

    from .version1.views import admin
    app.register_blueprint(admin.BP)

    return app
