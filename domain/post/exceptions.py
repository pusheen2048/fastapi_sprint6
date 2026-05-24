class BaseException(Exception):
    def __init__(self, detail):
        self.detail = detail

    def get_detail(self):
        return self.detail


class PostNotFoundByIdException(BaseException):
    def __init__(self, post_id):
        text = f'Пост с id {post_id} не найден.'
        super().__init__(text)


class PostDeleteForbiddenException(BaseException):
    def __init__(self, post_id):
        text = f'Пост с id {post_id} создан не Вами, поэтому Вы не можете его удалить.'
        super().__init__(text)


class PostEditForbiddenException(BaseException):
    def __init__(self, post_id):
        text = f'Пост с id {post_id} создан не Вами, поэтому Вы не можете прикрепить к нему изображение.'
        super().__init__(text)
