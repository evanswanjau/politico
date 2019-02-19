""" User implementation module """
from flask.views import MethodView
from flask import make_response, jsonify, request
from ...modules.user_module import UserModule
class UserAPI(MethodView):
    """ User Class Methods and Attributes """

    def post(self, action):
        data = request.get_json()
        current_user = UserModule(data)

        # sign up user
        if action == 'signup':
            new_user = current_user.signupUser()
            return make_response(jsonify({
                "status": 200,
                "data": new_user
                }), 200)
        elif action == 'login':
            data = current_user.loginUser()
            return make_response(jsonify({
                "status": 200,
                "data": data
                }), 200)
        else:
            pass
