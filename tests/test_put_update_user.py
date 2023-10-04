from tests.config import UserService
from tests.static import Errors


def test_update_user(create_test_users_body, generate_email, generate_name):
    r = UserService().post_user(data=create_test_users_body)

    assert r.status_code == 201

    user_id = r.json()['result']['id']
    create_test_users_body["name"] = generate_name
    create_test_users_body["email"] = generate_email
    create_test_users_body["customer_type"] = "private"

    r = UserService().update_user(data=create_test_users_body, user_id=user_id)

    assert r.status_code == 400
    print(r.json())


def test_update_non_existent_user(create_test_users_body, generate_email, generate_name):
    r = UserService().post_user(data=create_test_users_body)
    assert r.status_code == 201

    create_test_users_body["name"] = generate_name
    create_test_users_body["email"] = generate_email
    create_test_users_body["customer_type"] = "private"

    r = UserService().update_user(data=create_test_users_body, user_id=12345)

    assert r.status_code == 400
    print(r.json)


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
    print(r.json())


def test_update_user_duplicate_email(create_test_users_body, generate_name):
    r = UserService().post_user(data=create_test_users_body)

    assert r.status_code == 201

    user_id_new = r.json()['result']['id']

    create_test_users_body["email"] = "test_user512@gmail.com"
    create_test_users_body["name"] = generate_name
    create_test_users_body["customer_type"] = "private"
    r = UserService().update_user(data=create_test_users_body, user_id=user_id_new)
    assert r.status_code == 400

