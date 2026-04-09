class BaseException(Exception):
    def __init__(self, detail):
        self.detail = detail

    def get_detail(self):
        return self.detail


class UserNotFoundByUsernameException(BaseException):
    def __init__(self, username):
        text = f'Пользователь с логином {username} не найден'
        super().__init__(text)


class UserExistsException(BaseException):
    def __init__(self, username):
        text = f'Пользователь с логином {username} уже существует'
        super().__init__(text)
