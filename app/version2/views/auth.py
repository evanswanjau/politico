""" This is the user api implemetation section """
from flask import Blueprint
from ..views.api_modules.api_module import *

auth_bp = Blueprint('auth', __name__, url_prefix='/api/v2/auth/')

user_view = UserAPI.as_view('user_api')

# sign up user
auth_bp.add_url_rule('/signup', defaults={'action': 'signup'}, view_func=user_view, methods=['POST'])
