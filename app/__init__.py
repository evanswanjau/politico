import os

from flask import Flask, make_response, jsonify

def create_app(test_config=None):
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


    # error handdling
    @app.errorhandler(400)
    def bad_request(error):
        return make_response(jsonify({'status': 400, 'error': 'Invalid Request'}), 400)

    @app.errorhandler(403)
    def forbidden_request(error):
        return make_response(jsonify({'status': 403, 'error': 'Account Inaccessible'}), 403)

    @app.errorhandler(404)
    def page_not_found(error):
        return make_response(jsonify({'status': 404, 'error': 'Not Found'}), 404)

    @app.errorhandler(405)
    def not_allowed(error):
        return make_response(jsonify({'status': 405, 'error': 'Not Allowed'}), 405)

    @app.errorhandler(409)
    def already_exists(error):
        return make_response(jsonify({'status': 409, 'error': 'Already Exists'}), 409)

    # a simple page that says hello
    @app.route('/')
    def hello():
        return 'Hello, World!'

    from .version1.views import admin
    app.register_blueprint(admin.bp)

    return app
