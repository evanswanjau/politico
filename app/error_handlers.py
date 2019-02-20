
""" Custom Error Handling Modules """

class BaseError(Exception):
    """ Base Error Class """

    def __init__(self, status_code=400, message='', c_message=None):
        Exception.__init__(self)
        self.code = status_code
        self.message = message
        self.c_message = c_message

    def to_dict(self):
        if self.c_message:
            message = self.c_message
        else:
            message = self.message
        return {'status': self.code, 'message': message}


class NotFoundError(BaseError):
    def __init__(self, c_message, message='Not found'):
        BaseError.__init__(self)
        self.code = 404
        self.message = message
        self.c_message = c_message


class ValidationError(BaseError):
    def __init__(self, c_message, message='Invalid input'):
        BaseError.__init__(self)
        self.code = 400
        self.message = message
        self.c_message = c_message

class ConflictError(BaseError):
    def __init__(self, c_message, message='Already Exists'):
        BaseError.__init__(self)
        self.code = 409
        self.message = message
        self.c_message = c_message

class PermissionError(BaseError):
    def __init__(self, c_message, message='Permission denied'):
        BaseError.__init__(self)
        self.code = 403
        self.message = message
        self.c_message = c_message

class ForbiddenError(BaseError):
    def __init__(self, c_message, message='Access Denied'):
        BaseError.__init__(self)
        self.code = 403
        self.message = message
        self.c_message = c_message

class MethodError(BaseError):
    def __init__(self, c_message, message='Method not allowed'):
        BaseError.__init__(self)
        self.code = 405
        self.message = message
        self.c_message = c_message

class ServerError(BaseError):
    def __init__(self, message='Internal server error'):
        BaseError.__init__(self)
        self.code = 500
        self.message = message
        self.c_message = c_message
