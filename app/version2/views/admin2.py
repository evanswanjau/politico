""" This is all the api the admin is in charge of """

from flask import Blueprint
from ..views.api_modules.admin_api_module import *

admin2_bp = Blueprint('admin2', __name__, url_prefix='/api/v2/')

party_view = PartyAPI.as_view('political_party_api')

# view all political parties
admin2_bp.add_url_rule('/parties/', defaults={'party_id': None},
                      view_func=party_view, methods=['GET'])

# view single political party
admin2_bp.add_url_rule('/parties/<int:party_id>', view_func=party_view, methods=['GET'])

# post a new political party
admin2_bp.add_url_rule('/parties', view_func=party_view, methods=['POST'])

# edit a political party
admin2_bp.add_url_rule('/parties/<int:party_id>/name', view_func=party_view, methods=['PATCH'])

# delete a political party
admin2_bp.add_url_rule('/parties/<int:party_id>/', view_func=party_view, methods=['DELETE'])

"""
Political Offices
"""

office_view = OfficeAPI.as_view('political_office_api')

# post a new political office
admin2_bp.add_url_rule('/offices', view_func=office_view, methods=['POST'])

# view all political offices
admin2_bp.add_url_rule('/offices', defaults={'office_id': None},
                      view_func=office_view, methods=['GET'])

# view single political office
admin2_bp.add_url_rule('/offices/<int:office_id>', view_func=office_view, methods=['GET'])
