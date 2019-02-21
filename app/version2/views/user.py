""" This is the user api implemetation section """
from flask import Blueprint
from ..views.api_modules.api_module import *

user_bp = Blueprint('user', __name__, url_prefix='/api/v2/')

user_view = UserAPI.as_view('user_api')

# register candidate
user_bp.add_url_rule('/office/<int:office_id>/register', defaults={'action': 'register'},
                     view_func=user_view, methods=['POST'])

# user vote
user_bp.add_url_rule('/votes/', defaults={'action': 'vote'},
                     view_func=user_view, methods=['POST'])

# view all political office results
user_bp.add_url_rule('/office/<office_id>/result', defaults={'office_id': None},
                      view_func=user_view, methods=['GET'])

# request petition
user_bp.add_url_rule('/petitions/', defaults={'action': 'petition'},
                      view_func=user_view, methods=['POST'])
