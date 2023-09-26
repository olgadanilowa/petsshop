from tests.config import UserService
from tests.static import SuccessResponse, Errors


def _succesful_check(r, create_test_users_body):
    assert r.status_code == 201
    assert r.json()['message'] == SuccessResponse.created['message']
    assert r.json()['result']['name'] == create_test_users_body['name']
    assert r.json()['result']['email'] == create_test_users_body['email']
    assert r.json()['result']['date_birth'] == create_test_users_body['date_birth']


def test_create_user_success(create_test_users_body):
    r = UserService().post_user(data=create_test_users_body)

    _succesful_check(r, create_test_users_body)


def test_create_exists_user(create_test_users_body):
    r = UserService().post_user(data=create_test_users_body)

    _succesful_check(r, create_test_users_body)

    r = UserService().post_user(data=create_test_users_body)

    assert r.status_code == 400
    assert r.json() == Errors.user_exists


def test_create_user_without_name(create_test_users_body):
    data = create_test_users_body
    data.pop("name")

    r = UserService().post_user(data=data)

    assert r.status_code == 400
    assert r.json() == Errors.empty_field


def test_create_user_empty_body():
    r = UserService().post_user(data={})

    assert r.status_code == 400
    assert r.json() == Errors.empty_field


def test_creating_and_getting_user_info(create_test_users_body):
    response = UserService().post_user(data=create_test_users_body)

    response = response.json()

    user_id = response['result']['id']
    response = UserService().get_user_id(user_id)
    user_data = response.json()


def test_create_user_without_date_birth(create_test_users_body):
    data = create_test_users_body
    data.pop("date_birth")

    r = UserService().post_user(data=data)

    assert r.status_code == 201

