import os

from flask import Flask, make_response, jsonify

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # a simple page that says hello
    @app.route('/')
    def hello():
        return 'Hello, World!'

    from .version1.views import admin
    app.register_blueprint(admin.bp)

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




    return app
