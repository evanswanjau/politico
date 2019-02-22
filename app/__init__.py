""" This is the Application Initialization Method """
import os
from flask import Flask, make_response, jsonify
from werkzeug.exceptions import HTTPException
from instance.config import app_config
from app.error_handlers import *
from .version1.views import admin
from .version2.views import admin2
from .version2.views import auth
from .version2.views import user
from .db.database import DBConnection

def create_app(test_config=None):
    """ Method to Build The APP """
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(os.getenv("APP_SETTING"))
    app.config['JWT_SECRET_KEY'] = 'ThisismylilSecret'
    jwt = JWTManager(app)

    app.config.from_pyfile('config.py')
    DB_URL = os.getenv("DATABASE_URL")

    db = DBConnection(DB_URL)

    # drop existing tables, create new ones and add admin
    db.drop_tables()
    db.create_tables_and_admin()

    # error handlers
    @app.errorhandler(ConflictError)
    @app.errorhandler(ValidationError)
    @app.errorhandler(ConflictError)
    @app.errorhandler(PermissionError)
    @app.errorhandler(MethodError)
    @app.errorhandler(ServerError)
    @app.errorhandler(NotFoundError)
    @app.errorhandler(ForbiddenError)
    @app.errorhandler(BaseError)
    def handle_error(error):
        return make_response(jsonify(error.to_dict()), error.code)

    #This will catch any uncaught http error
    @app.errorhandler(Exception)
    def exceptional_error(error):
        if isinstance(error, HTTPException):
            return make_response(jsonify(status=error.code, message=error.description), error.code)

    # the app home page
    @app.route('/')
    def hello():
        return 'Welcome to Politico'


    # admin blueprint
    app.register_blueprint(admin.admin_bp)
    # admin blueprint
    app.register_blueprint(admin2.admin2_bp)
    # auth blueprint
    app.register_blueprint(auth.auth_bp)
    # user blueprint
    app.register_blueprint(user.user_bp)

    return app
