from tests.config import UserService


def test_create_user_success():
    data = {"name": "pupkin", "email": "pupkin@mail.ru", "date_birth": "01.01.01"}
    r = UserService().post_user(data=data)
    print(r)


def test_create_exists_user():
    data = {"name": "pupkin", "email": "pupkin@mail.ru", "date_birth": "01.01.01"}
    r = UserService().post_user_fail(data=data)
    print(r)

def test_create_user_without_name():
    data = {"name": "pupkin", "email": "pu08888@maipp0pl.ru", "date_birth": "88.99.00"}
    r = UserService().post_user_fail(data=data)
    print(r)
