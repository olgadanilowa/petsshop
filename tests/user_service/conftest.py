import random

import pytest
import requests

from tests.user_service.config import UserService


@pytest.fixture
def generate_password():
    password = "password" + str(random.randint(1, 10000) + 1)
    return password


@pytest.fixture
def generate_email():
    email = "test_user" + str(random.randint(1, 10000) + 1) + "@" + random.choice(
        ["mail.ru", "gmail.com", "yandex.ru"])
    return email


@pytest.fixture
def generate_name():
    name = "test_user" + str(random.randint(1, 10000) + 1)
    return name


@pytest.fixture
def create_test_users_body(generate_email, generate_name, generate_password):
    users = {}
    users["name"] = generate_name
    users["email"] = generate_email
    users["date_birth"] = str(random.randint(1923, 2023)) + "." + str(random.randint(1, 12)) + "." + str(
        random.randint(1, 31))
    users["customer_type"] = random.choice(["private", "company"])
    users["password"] = generate_password
    return users


@pytest.fixture
def create_and_login_user(create_test_users_body):
    user_body = create_test_users_body

    create_user = UserService().post_user(data=user_body)

    assert create_user.status_code == 201

    login_body = {
        "email": user_body["email"],
        "password": user_body["password"]
    }

    login_user = UserService().user_login(data=login_body)

    assert login_user.status_code == 200

    login_response = login_user.json()
    user_info = login_response['result']
    token = login_response['result']['token']

    return user_info, token, create_test_users_body
