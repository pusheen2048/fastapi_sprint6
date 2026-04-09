class BaseException(Exception):
    def __init__(self, detail):
        self.detail = detail

    def get_detail(self):
        return self.detail


class CategoryNotFoundByTitleException(BaseException):
    def __init__(self, title):
        text = f'Категория с названием {title} не найдена'
        super().__init__(text)


class CategoryExistsException(BaseException):
    def __init__(self, title):
        text = f'Категория с названием {title} уже существует'
        super().__init__(text)
