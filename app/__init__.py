""" This is the Application Initialization Method """
import os
from flask import Flask, make_response, jsonify
from instance.config import app_config
from app.error_handlers import *
from .version1.views import admin
from .version2.views import auth
from .db.database import DBConnection

def create_app(test_config=None):
    """ Method to Build The APP """
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(os.getenv("APP_SETTING"))
    app.config.from_pyfile('config.py')
    DB_URL = "politico_db, user=postgres, password=pass123, host=127.0.0.1, port=5432"

    DBConnection(DB_URL)
    DBConnection.create_tables_and_admin(DBConnection)
    if name_conf == "testing":
        DbConnection.drop_all_tables(DBConnection)


    # error handlers
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
        return error, 'error here'


    # the app home page
    @app.route('/')
    def hello():
        return 'Welcome to Politico'


    # admin blueprint
    app.register_blueprint(admin.admin_bp)
    # auth blueprint
    app.register_blueprint(auth.auth_bp)

    return app
