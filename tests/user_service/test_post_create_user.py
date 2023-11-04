from tests.user_service.config import UserService
from tests.user_service.db_config import DbConnect
from tests.user_service.static import SuccessResponse, Errors


def _succesful_check(r, create_test_users_body):
    print(r.json())
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
    assert r.json() == Errors.incorrect_fields


def test_create_user_empty_body():
    r = UserService().post_user(data={})

    assert r.status_code == 400
    assert r.json() == Errors.incorrect_fields


def test_creating_and_getting_user_info(create_test_users_body):
    response = UserService().post_user(data=create_test_users_body)
    assert response.status_code == 201
    email = response.json()['result']['email']
    password = response.json()['result']['password']
    user_id = response.json()['result']['id']

    data = {
        'email': email,
        'password': password
    }

    r = UserService().user_login(data=data)

    assert r.status_code == 200

    token = DbConnect().select_user_by_id(user_id=user_id)[0][6]
    response = UserService().get_user_id(user_id=user_id, headers={})

    assert response.status_code == 400

    '''user_data = response.json()
    user_db_data = DbConnect().select_user_by_id(user_id=user_id)

    assert user_data['result']['name'] == user_db_data[0][1]
    assert user_data['result']['email'] == user_db_data[0][2]
    assert user_data['result']['customer_type'] == user_db_data[0][4]'''


def test_create_user_without_date_birth(create_test_users_body):
    data = create_test_users_body
    data.pop("date_birth")

    r = UserService().post_user(data=data)

    assert r.status_code == 201


def test_create_user_without_company(create_test_users_body):
    data = create_test_users_body
    data.pop("customer_type")

    r = UserService().post_user(data=data)

    assert r.status_code == 400


def test_create_user_wrong_customer_type(create_test_users_body):
    data = create_test_users_body
    data["customer_type"] = "opop"

    r = UserService().post_user(data=data)

    assert r.status_code == 400
