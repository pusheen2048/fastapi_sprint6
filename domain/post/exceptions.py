class BaseException(Exception):
    def __init__(self, detail):
        self.detail = detail

    def get_detail(self):
        return self.detail


class PostNotFoundByTitleException(BaseException):
    def __init__(self, title):
        text = f'Пост с названием {title} не найден'
        super().__init__(text)


class PostExistsException(BaseException):
    def __init__(self, title):
        text = f'Пост с названием {title} уже существует'
        super().__init__(text)
