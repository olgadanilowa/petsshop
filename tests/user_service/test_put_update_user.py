import random
from copy import deepcopy

from tests.user_service.config import UserService
from tests.user_service.static import Errors


def _generate_email():
    email = "test_user" + str(random.randint(1, 10000) + 1) + "@" + random.choice(
        ["mail.ru", "gmail.com", "yandex.ru"])
    return email


def _generate_name():
    name = "test_user" + str(random.randint(1, 10000) + 1)
    return name


def test_update_user(create_and_login_user, generate_email, generate_name):
    headers = {
        'email': create_and_login_user[0]['email'],
        'x-auth-token': create_and_login_user[1]
    }
    user_body = deepcopy(create_and_login_user[0])
    user_body["name"] = generate_name
    user_body["company_type"] = "private"

    r = UserService().update_user(data=user_body, user_id=create_and_login_user[0]["id"], headers=headers)

    assert r.status_code == 200

    updated_user_body = r.json()['result']
    assert updated_user_body["name"] == generate_name
    assert updated_user_body["customer_type"] == user_body["customer_type"]


def test_update_non_existent_user(create_test_users_body, generate_email, generate_name):
    r = UserService().post_user(data=create_test_users_body)

    assert r.status_code == 201

    create_test_users_body["name"] = generate_name
    create_test_users_body["email"] = generate_email
    create_test_users_body["customer_type"] = "private"

    r = UserService().update_user(data=create_test_users_body, user_id=12345)

    assert r.status_code == 400
    assert r.json() == Errors.user_not_found


def test_update_user_long_date_birth(create_test_users_body, generate_email, generate_name):
    r = UserService().post_user(data=create_test_users_body)

    assert r.status_code == 201

    user_id = r.json()['result']['id']
    create_test_users_body["name"] = generate_name
    create_test_users_body["email"] = generate_email
    create_test_users_body["customer_type"] = "private"
    create_test_users_body["date_birth"] = "1998.5.23456"

    r = UserService().update_user(data=create_test_users_body, user_id=user_id)

    assert r.status_code == 400
    assert r.json() == Errors.incorrect_fields


'''def test_update_user_duplicate_email(create_test_users_body, generate_name):
    r = UserService().post_user(data=create_test_users_body)

    assert r.status_code == 201

    create_test_users_body_new = deepcopy(create_test_users_body)
    create_test_users_body_new["email"] = "test_user512@gmail.com"
    create_test_users_body_new["name"] = generate_name
    create_test_users_body_new["customer_type"] = "private"
    r1 = UserService().post_user(data=create_test_users_body_new)
    assert r1.status_code == 201
    user_id_new = r1.json()['result']['id']
    r2 = UserService().update_user(data=create_test_users_body, user_id=user_id_new)

    assert r.status_code == 400'''


def test_update_user_duplicate_email(create_test_users_body):


    r = UserService().post_user(data=create_test_users_body)

    assert r.status_code == 201

    create_test_users_body_new = deepcopy(create_test_users_body)
    create_test_users_body_new["email"] = _generate_email()
    create_test_users_body_new["name"] = _generate_name()
    create_test_users_body_new["customer_type"] = "private"
    r1 = UserService().post_user(data=create_test_users_body_new)

    assert r1.status_code == 201

    user_id_new = r1.json()['result']['id']
    r2 = UserService().update_user(data=create_test_users_body, user_id=user_id_new)

    assert r2.status_code == 400
