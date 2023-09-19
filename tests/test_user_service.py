from tests.config import UserService


def test_create_user():
    data={
    "name": "pupkpin",
    "email": "pupkin@maipppl.ru",
    "date_birth": "01.01.01"
}
    r=UserService().post_user(data=data)
    print(r)

