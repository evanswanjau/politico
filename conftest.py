import pytest
from flask import Flask, current_app
from app import create_app

app = Flask(__name__)

with app.app_context():
    app = current_app._get_current_object()


@pytest.fixture
def app():
    app = create_app()
    return app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()
