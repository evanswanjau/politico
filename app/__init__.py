""" This is the Application Initialization Method """
import os
from flask import Flask, make_response, jsonify
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
from instance.config import app_config
from app.error_handlers import *
from .version1.views import admin
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
        return make_response(jsonify(error.to_dict()))

    # This will catch any uncaught http error


    # the app home page
    @app.route('/')
    def hello():
        return 'Welcome to Politico'


    # admin blueprint
    app.register_blueprint(admin.admin_bp)
    # auth blueprint
    app.register_blueprint(auth.auth_bp)
    # user blueprint
    app.register_blueprint(user.user_bp)

    return app
