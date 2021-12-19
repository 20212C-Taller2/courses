class UserError(Exception):
    def __init__(self, code: str, message: str):
        self.code = code
        self.message = message
        super().__init__(self.code, self.message)

    def __str__(self):
        return self.message


class UserNotFoundError(UserError):
    def __init__(self, name: str):
        super(UserNotFoundError, self).__init__('CREATOR_NOT_FOUND', f'User {name} not found')
